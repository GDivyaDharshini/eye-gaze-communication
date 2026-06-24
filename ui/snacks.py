import streamlit as st

def snacks_page():

    st.header("🍟 Snacks")

    st.warning("👀 Look in a direction to select")

    # UP
    top = st.columns([1,2,1])

    with top[1]:
        if st.button("🍪 Cookies"):
            st.session_state.message = "I need Cookies"

    # LEFT - CENTER - RIGHT
    middle = st.columns(3)

    with middle[0]:
        if st.button("🥨 Biscuits"):
            st.session_state.message = "I need Biscuits"

    with middle[1]:
        st.info("👁️ LOOK HERE")

    with middle[2]:
        if st.button("🍟 Chips"):
            st.session_state.message = "I need Chips"

    # DOWN
    bottom = st.columns([1,2,1])

    with bottom[1]:
        if st.button("🍰 Cake"):
            st.session_state.message = "I need Cake"

    # Back Button
    if st.button("⬅ Back"):
        st.session_state.page = "food"
        st.rerun()