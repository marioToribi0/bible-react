from langchain_pinecone import PineconeVectorStore
from langchain.agents import tool
from langchain_openai import OpenAIEmbeddings
import os
from unidecode import unidecode
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(api_key=os.environ["OPENAI_API_KEY"])

@tool
def find_vers(query: str):
    """Buscar versiculos de la biblia a partir de un query. Usa palabras en especifico no preguntas, esto busca coincidencia de palabras con versiculos por lo que deberás tomar palabras correctas para llegar a la informacion que necesitas.
   "Recuerda que antes de que vayas a dar tu respuesta final uses modify_lecture"]

    Args:
        query (str): texto a buscar en la biblia

    Returns:
        str: versiculos
    """
    vectorstore = PineconeVectorStore(
            index_name=os.environ["INDEX_NAME"], embedding=embeddings
        )

    context = vectorstore.similarity_search(query)
    return f'{[context, "Recuerda que antes de que vayas a dar tu respuesta final uses modify_lecture"]}'
    
tools = [find_vers]