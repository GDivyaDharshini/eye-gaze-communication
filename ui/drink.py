import streamlit as st

from ui.translations import translations
from ui.dashboard_languages import dashboard_languages
def option_card(icon, title, direction):

    st.markdown(
        f"""
        <div class="food-card">
            <div class="food-icon">{icon}</div>
            <div class="food-title">{title}</div>
            <div class="food-direction">{direction}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def drink_page():

    lang = dashboard_languages[st.session_state.language]

    st.title("🥤 " + lang["DRINKS"])

    # ---------------- TOP ----------------

    top = st.columns([1,2,1])

    with top[1]:

        option_card("💧", "WATER", "↑ Look Up")

        if st.button("Select Water", use_container_width=True):

            lang = st.session_state.language
            st.session_state.selected_item = "water"

            st.session_state.message = translations["water"][language]

            st.session_state.page = "confirmation"

            st.rerun()


    st.write("")

    # ---------------- MIDDLE ----------------

    left, center, right = st.columns([2,1,2])

    with left:

        option_card("☕", "COFFEE", "◀ Look Left")

        if st.button("Select Coffee", use_container_width=True):

            lang = st.session_state.language
            st.session_state.selected_item = "coffee"

            st.session_state.message = translations["coffee"][language]

            st.session_state.page = "confirmation"


            st.rerun()

    with center:

        st.markdown(
            """
            <div class="eye-center">
                👁
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        option_card("🧃", "JUICE", "Look Right ▶")

        if st.button("Select Juice", use_container_width=True):

            lang = st.session_state.language
            st.session_state.selected_item = "juice"

            st.session_state.message = translations["juice"][language]

            st.session_state.page = "confirmation"

            st.rerun()
            

    st.write("")

    # ---------------- BOTTOM ----------------

    bottom = st.columns([1,2,1])

    with bottom[1]:

        option_card("🥛", "MILK", "↓ Look Down")

        if st.button("Select Milk", use_container_width=True):

            lang = st.session_state.language
            st.session_state.selected_item = "milk"

            st.session_state.message = translations["milk"][language]

            st.session_state.page = "confirmation"

            
            st.rerun()

    st.write("")

    if st.button(lang["BACK"], use_container_width=True):

        st.session_state.page = "menu"
        st.rerun()