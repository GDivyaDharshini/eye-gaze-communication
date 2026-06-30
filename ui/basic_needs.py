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


def basic_needs_page():

    lang = dashboard_languages[st.session_state.language]

    st.title("🛏 " + lang["BASIC_NEEDS"])

    # ---------------- TOP ----------------

    top = st.columns([1, 2, 1])

    with top[1]:

        option_card("🚻", "WASHROOM", "↑ Look Up")

        if st.button("Select Washroom", use_container_width=True):

            st.session_state.selected_item = "Washroom"
            st.session_state.message = translations["Washroom"][st.session_state.language]
            st.session_state.page = "confirmation"
            st.rerun()

    st.write("")

    # ---------------- MIDDLE ----------------

    left, center, right = st.columns([2, 1, 2])

    with left:

        option_card("😴", "SLEEP", "◀ Look Left")

        if st.button("Select Sleep", use_container_width=True):

            st.session_state.selected_item = "Sleep"
            st.session_state.message = translations["Sleep"][st.session_state.language]
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

        option_card("😖", "PAIN", "Look Right ▶")

        if st.button("Select Pain", use_container_width=True):

            st.session_state.selected_item = "Pain"
            st.session_state.message = translations["Pain"][st.session_state.language]
            st.session_state.page = "confirmation"
            st.rerun()

    st.write("")

    # ---------------- BOTTOM ----------------

    bottom = st.columns([1, 2, 1])

    with bottom[1]:

        option_card("🍽️", "HUNGRY", "↓ Look Down")

        if st.button("Select Hungry", use_container_width=True):

            st.session_state.selected_item = "Hungry"
            st.session_state.message = translations["Hungry"][st.session_state.language]
            st.session_state.page = "confirmation"
            st.rerun()

    st.write("")

    if st.button(lang["BACK"], use_container_width=True):

        st.session_state.page = "menu"
        st.rerun()