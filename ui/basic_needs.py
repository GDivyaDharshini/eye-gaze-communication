import streamlit as st

def basic_needs_page():

    st.header("🛏️ Basic Needs")

    st.warning("👀 Look in a direction to select")

    top = st.columns([1,2,1])

    with top[1]:
        if st.button("🚻 Washroom"):
            st.session_state.message = "I need Washroom"

    middle = st.columns(3)

    with middle[0]:
        if st.button("😣 Pain"):
            st.session_state.message = "I am in Pain"

    with middle[1]:
        st.info("👁️ LOOK HERE")

    with middle[2]:
        if st.button("🙋 Help"):
            st.session_state.message = "I need Help"

    bottom = st.columns([1,2,1])

    with bottom[1]:
        if st.button("😴 Sleep"):
            st.session_state.message = "I want to Sleep"

    if st.button("⬅ Back"):
        st.session_state.page = "menu"
        st.rerun()