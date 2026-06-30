import streamlit as st

from utils.speech import speak
from ui.dashboard_languages import dashboard_languages


def confirmation_page():

    lang = dashboard_text[st.session_state.language]

    st.title("✅ Confirmation")

    st.markdown("## Selected Message")

    st.markdown(
        f"""
        <div class="message-box">
            💬 {st.session_state.message}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.info("👤 Nod your head for YES or Shake your head for NO")

    st.write("")

    col1, col2 = st.columns(2)

    # ------------------------
    # YES
    # ------------------------

    with col1:

        if st.button("👍 YES", use_container_width=True):

            speak(st.session_state.message)

            st.success("Message Spoken Successfully")

            st.session_state.page = "menu"

            st.session_state.selected_item = ""

            st.session_state.message = "---"

            st.rerun()

    # ------------------------
    # NO
    # ------------------------

    with col2:

        if st.button("👎 NO", use_container_width=True):

            previous = st.session_state.selected_item.lower()

            if previous == "snacks":
                st.session_state.page = "snacks"

            elif previous in ["idli", "dosa", "chapati"]:
                st.session_state.page = "food"

            elif previous in ["water", "coffee", "juice", "milk"]:
                st.session_state.page = "drink"

            elif previous in ["washroom", "sleep", "pain", "hungry"]:
                st.session_state.page = "basic_needs"

            elif previous in ["help", "doctor", "fire", "call home"]:
                st.session_state.page = "emergency"

            else:
                st.session_state.page = "menu"

            st.rerun()