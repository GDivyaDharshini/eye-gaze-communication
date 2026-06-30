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


def emergency_page():

    lang = dashboard_languages[st.session_state.language]

    st.title("🚨 " + lang["EMERGENCY"])

    # ---------------- TOP ----------------

    top = st.columns([1, 2, 1])

    with top[1]:

        option_card("🆘", "HELP", "↑ Look Up")

        if st.button("Select Help", use_container_width=True):

            st.session_state.selected_item = "Help"
            st.session_state.message = translations["Help"][st.session_state.language]
            st.session_state.page = "confirmation"
            st.rerun()

    st.write("")

    # ---------------- MIDDLE ----------------

    left, center, right = st.columns([2, 1, 2])

    with left:

        option_card("👨‍⚕️", "DOCTOR", "◀ Look Left")

        if st.button("Select Doctor", use_container_width=True):

            st.session_state.selected_item = "Doctor"
            st.session_state.message = translations["Doctor"][st.session_state.language]
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

        option_card("🔥", "FIRE", "Look Right ▶")

        if st.button("Select Fire", use_container_width=True):

            st.session_state.selected_item = "Fire"
            st.session_state.message = translations["Fire"][st.session_state.language]
            st.session_state.page = "confirmation"
            st.rerun()

    st.write("")

    # ---------------- BOTTOM ----------------

    bottom = st.columns([1, 2, 1])

    with bottom[1]:

        option_card("📞", "CALL HOME", "↓ Look Down")

        if st.button("Select Call Home", use_container_width=True):

            st.session_state.selected_item = "Call Home"
            st.session_state.message = translations["Call Home"][st.session_state.language]
            st.session_state.page = "confirmation"
            st.rerun()

    st.write("")

    if st.button(lang["BACK"], use_container_width=True):

        st.session_state.page = "menu"
        st.rerun()