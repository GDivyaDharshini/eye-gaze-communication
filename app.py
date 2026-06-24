import streamlit as st
from ui.menu import show_menu

# Page settings
st.set_page_config(
    page_title="GazeConnect",
    layout="wide"
)

# Session state
if "page" not in st.session_state:
    st.session_state.page = "menu"

if "message" not in st.session_state:
    st.session_state.message = "---"

# Header
st.title("👁️ GazeConnect")
st.subheader("Eye Controlled Communication System")
# Language Selector
language = st.selectbox(
    "🌐 Language",
    ["English", "Tamil", "Hindi", "Bengali"]
)

st.session_state.language = language

# Selected message area
st.markdown("### Selected Message")
st.markdown("### 🗣 Communication Output")
st.success(st.session_state.message)
# Show current page
show_menu(st.session_state.page)