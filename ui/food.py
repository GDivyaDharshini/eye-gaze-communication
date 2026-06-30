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


def food_page():

    lang = dashboard_languages[st.session_state.language]
    current_direction = st.session_state.direction

    st.title("🍔 " + lang["FOOD"])

    # ---------------- TOP ----------------

    top = st.columns([1, 2, 1])

    with top[1]:

        option_card("🍛", "IDLI", "↑ Look Up")

        if st.button("Select Idli", use_container_width=True):

            st.session_state.selected_item = "Idli"
            st.session_state.message = translations["Idli"][st.session_state.language]
            st.session_state.page = "confirmation"
            st.rerun()

    st.write("")

    # ---------------- MIDDLE ----------------

    left, center, right = st.columns([2, 1, 2])

    with left:

        option_card("🥞", "DOSA", "◀ Look Left")

        if st.button("Select Dosa", use_container_width=True):

            st.session_state.selected_item = "Dosa"
            st.session_state.message = translations["Dosa"][st.session_state.language]
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

        option_card("🫓", "CHAPATI", "Look Right ▶")

        if st.button("Select Chapati", use_container_width=True):

            st.session_state.selected_item = "Chapati"
            st.session_state.message = translations["Chapati"][st.session_state.language]
            st.session_state.page = "confirmation"
            st.rerun()

    st.write("")

    # ---------------- BOTTOM ----------------

    bottom = st.columns([1, 2, 1])

    with bottom[1]:

        option_card("🍟", "SNACKS", "↓ Look Down")

        if st.button("Open Snacks", use_container_width=True):

            st.session_state.page = "snacks"
            st.rerun()

    st.write("")

    if st.button(lang["BACK"], use_container_width=True):

        st.session_state.page = "menu"
        st.rerun()