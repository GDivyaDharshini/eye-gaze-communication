from ui.translations import translations
import streamlit as st
st.info("👁️ LOOK HERE")
def food_page():

    st.header("🍔 Food")

    top = st.columns([1,2,1])

    with top[1]:
         st.markdown("""
    <div style="
    padding:20px;
    border-radius:15px;
    background:#F3EEFF;
    text-align:center;
    font-size:30px;
    ">
    🍚<br><b>Idli</b>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Select Idli"):
        lang = st.session_state.get("language", "English")
        st.session_state.message = translations["Idli"][lang]

    middle = st.columns(3)

    with middle[0]:
        if st.button("🥞 Dosa"):
            lang = st.session_state.get("language", "English")
            st.session_state.message = translations["Dosa"][lang]

    with middle[1]:
        st.info("👁️ LOOK HERE")

    with middle[2]:
        if st.button("🫓 Chapati"):
            lang = st.session_state.get("language", "English")
            st.session_state.message = translations["Chapati"][lang]

    bottom = st.columns([1,2,1])

    with bottom[1]:
        
         if st.button("🍟 Snacks"):
            lang = st.session_state.get("language", "English")
            st.session_state.message = translations["Snacks"][lang]

            st.session_state.page = "snacks"
            st.rerun()

    if st.button("⬅ Back"):
        st.session_state.page = "menu"
        st.rerun()