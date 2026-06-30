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


def snacks_page():

    lang = dashboard_languages[st.session_state.language]

    st.title("🍟 " + lang["SNACKS"])

    # ---------------- TOP ----------------

    top = st.columns([1, 2, 1])

    with top[1]:

        option_card("🍪", "BISCUIT", "↑ Look Up")

        if st.button("Select Biscuit", use_container_width=True):

            st.session_state.selected_item = "Biscuit"
            st.session_state.message = translations["Biscuit"][st.session_state.language]
            st.session_state.page = "confirmation"
            st.rerun()

    st.write("")

    # ---------------- MIDDLE ----------------

    left, center, right = st.columns([2, 1, 2])

    with left:

        option_card("🍿", "POPCORN", "◀ Look Left")

        if st.button("Select Popcorn", use_container_width=True):

            st.session_state.selected_item = "Popcorn"
            st.session_state.message = translations["Popcorn"][st.session_state.language]
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

        option_card("🍫", "CHOCOLATE", "Look Right ▶")

        if st.button("Select Chocolate", use_container_width=True):

            st.session_state.selected_item = "Chocolate"
            st.session_state.message = translations["Chocolate"][st.session_state.language]
            st.session_state.page = "confirmation"
            st.rerun()

    st.write("")

    # ---------------- BOTTOM ----------------

    bottom = st.columns([1, 2, 1])

    with bottom[1]:

        option_card("🍰", "CAKE", "↓ Look Down")

        if st.button("Select Cake", use_container_width=True):

            st.session_state.selected_item = "Cake"
            st.session_state.message = translations["Cake"][st.session_state.language]
            st.session_state.page = "confirmation"
            st.rerun()

    st.write("")

    if st.button(lang["BACK"], use_container_width=True):

        st.session_state.page = "food"
        st.rerun()