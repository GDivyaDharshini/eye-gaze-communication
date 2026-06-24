import streamlit as st

def drink_page():

    st.header("🥤 Drinks")

    st.warning("👀 Look in a direction to select")

    # UP
    top = st.columns([1,2,1])

    with top[1]:
        if st.button("💧 Water"):
            st.session_state.message = "I need Water"

    # LEFT CENTER RIGHT
    middle = st.columns(3)

    with middle[0]:
        if st.button("☕ Tea"):
            st.session_state.message = "I need Tea"

    with middle[1]:
        st.info("👁️ LOOK HERE")

    with middle[2]:
        if st.button("🧃 Juice"):
            st.session_state.message = "I need Juice"

    # DOWN
    bottom = st.columns([1,2,1])

    with bottom[1]:
        if st.button("☕ Coffee"):
            st.session_state.message = "I need Coffee"

    if st.button("⬅ Back"):
        st.session_state.page = "menu"
        st.rerun()