from streamlit_javascript import st_javascript
from streamlit_js_eval import streamlit_js_eval
import json

def get_from_local_storage(k):
    v = st_javascript(
        f"JSON.parse(localStorage.getItem('{k}'));"
    )
    return None if v==0 else v


def set_to_local_storage(k, v):
    jdata = json.dumps(v)
    streamlit_js_eval(js_expressions=f"localStorage.setItem('{k}', JSON.stringify({jdata}));")

