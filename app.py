import streamlit as st
from ui.menu import show_menu

# Page Settings
st.set_page_config(
    page_title="GazeConnect",
    layout="wide"
)

# Session State
if "page" not in st.session_state:
    st.session_state.page = "menu"

if "message" not in st.session_state:
    st.session_state.message = "---"

if "language" not in st.session_state:
    st.session_state.language = "English"

# Header
st.title("👁️ GazeConnect")
st.subheader("Eye Controlled Communication System")

# Language Selector
language = st.selectbox(
    "🌐 Language",
    ["English", "Tamil", "Hindi", "Bengali"],
    index=["English", "Tamil", "Hindi", "Bengali"].index(
        st.session_state.language
    )
)

st.session_state.language = language

# Communication Output
st.markdown("### 🗣 Communication Output")
st.success(st.session_state.message)

# Show Current Page
show_menu(st.session_state.page)