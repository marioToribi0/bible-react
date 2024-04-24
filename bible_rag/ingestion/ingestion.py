from dotenv import load_dotenv
import xml.etree.ElementTree as ET
import pandas as pd
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
import os

def load_bible(all_bible=False) -> pd.DataFrame:
    tree = ET.parse('./rag_intro/static/data/reina_valera_bible.xml')
    root = tree.getroot()
    books = []
    chapters = []
    vers_num = []
    versiculos = []
    body = []
    for book in root[1:]:
        for chapter in book:
            for vers in chapter:
                books.append(f"{book.get('bname')}")
                vers_num.append(f"{vers.get('vnumber')}")
                chapters.append(f"{chapter.get('cnumber')}")
                versiculos.append(f"{book.get('bname')} {chapter.get('cnumber')}:{vers.get('vnumber')}")
                body.append(f"{vers.text}")
    res = pd.DataFrame({"Versículo":versiculos, "Contenido":body, "Book": books, "chapter": chapters, "vers_num": vers_num})
    res["res"] = res["Versículo"] + " " + res["Contenido"]
    if all_bible:
        return res
    else:
        return list(res["res"].values)


if __name__=="__main__":
    load_dotenv()
    print("Loading...")
    bible = load_bible()
    
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
    
    print("Ingesting...")
    PineconeVectorStore.from_texts(bible, embeddings, index_name=os.environ["INDEX_NAME"])
    
    print("Finish")
    