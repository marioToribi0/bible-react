import streamlit as st
from model.assistant import generate_response
from ingestion.ingestion import load_bible
from langchain_core.messages import AIMessage, HumanMessage
from concurrent.futures import ThreadPoolExecutor
from storage.local_storage import get_from_local_storage, set_to_local_storage
from modules.load_data import get_save_comparison

executor = ThreadPoolExecutor(max_workers=1)

st.cache_resource()
def load_data():
    bible = load_bible(all_bible=True)
    return {"bible": bible,
            "books": bible["Book"].value_counts(sort=False).index.to_list()}

def get_local_storage():
    with st.container():
        st.session_state["book"] = get_from_local_storage('book')
        st.session_state["toggle"] = get_from_local_storage('toggle')
        st.session_state["chapter"] = get_from_local_storage('chapter')

async def interface_assistant():
    # Streamed response emulator
    st.set_page_config("Biblia", page_icon="📙", layout="wide")
    st.title("Biblia 📙")
    get_local_storage()
    
    bible_data = load_data()
    bible = bible_data["bible"]

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)

    # Accept user input
    if prompt := st.chat_input("¿En qué te puedo ayudar?"):
        # Add user message to chat history
        st.session_state.messages.append(HumanMessage(content=prompt))
        # Display user message in chat message container
        with st.chat_message("Human"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("AI"):
            text = ""
            placeholder = st.empty()

            # async for chunk in generate_response(prompt=prompt, chat_history=st.session_state.messages):
            async for chunk in generate_response(
                **{"prompt": prompt, "chat_history": st.session_state.messages}
            ):
                text += chunk
                placeholder.markdown(text)
            response = text
        # Add assistant response to chat history
        st.session_state.messages.append(AIMessage(content=response))
    
    with st.sidebar:
        st.write("# Leer un versículo")
        allow = st.toggle("No modificar tu lectura", value=get_save_comparison(st.session_state.get("allow"), None, False))
        st.session_state["allow"] = allow

        book = st.selectbox("Libro", bible_data["books"], index=get_save_comparison(st.session_state.get("book"), None, 0))
        st.session_state["book"] = bible_data["books"].index(book)

        chapter = st.select_slider("Capítulo", [i+1 for i in range(int(bible[bible["Book"]==book]["chapter"].astype(int).max()))], value=get_save_comparison(st.session_state.get("chapter"), None, 1))

        # print(chapter)
        st.session_state["chapter"] = chapter

        filter_bible = bible[(bible["Book"]==book)&(bible["chapter"]==str(chapter))]
        
        st.divider()

        [st.write(f'{row["Contenido"]} **{row["vers_num"]}**') for idx, row in filter_bible[["Contenido", "vers_num"]].iterrows()]
        set_to_local_storage("allow", st.session_state["allow"])
        set_to_local_storage("book", st.session_state["book"])
        set_to_local_storage("chapter", st.session_state["chapter"])


