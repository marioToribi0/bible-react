from bible_react.interface.interface import interface_assistant
import asyncio
import streamlit as st
from dotenv import load_dotenv
from bible_react.storage.local_storage import get_from_local_storage
import hmac
import os

async def main():

    await interface_assistant()
    

def password_entered():
    """Checks whether a password entered by the user is correct."""
    if hmac.compare_digest(st.session_state.get("PASSWORD", ""), os.environ["PASSWORD"]):
        st.session_state["password_correct"] = True
    else:
        st.session_state["password_correct"] = False

def check_password():
    """Returns `True` if the user had the correct password."""
    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True
    
    st.text_input(
            "Password", type="password", on_change=password_entered, key="PASSWORD"
        )
    
    if (st.session_state.get("PASSWORD") is not None):
        # Show input for password.
        if "password_correct" in st.session_state:
            st.error("😕 Password incorrect")
    return False


if __name__ == "__main__":
    load_dotenv()
    st.set_page_config("Biblia", page_icon="📙", layout="wide")
    st.title("Biblia 📙")
    ## Loading Password
    
    result = get_from_local_storage("PASSWORD")
    if result is not None:
        st.session_state["PASSWORD"] = result
        if password_entered():
            asyncio.run(main())
    
    if not check_password():
        st.stop()

    asyncio.run(main())
    
    
        
