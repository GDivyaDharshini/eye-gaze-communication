import streamlit as st
import time

from ui.regions import REGIONS


# ---------------------------------------------------
# Selection Card (FIXED)
# ---------------------------------------------------
def selection_card(icon, title, subtitle, direction_text, code):

    # initialize session state
    if "direction" not in st.session_state:
        st.session_state.direction = None

    # active state
    active = (st.session_state.direction == code)

    border = "#4F8EF7" if active else "#E8EEF8"
    background = "#EEF5FF" if active else "white"

    # SINGLE BUTTON (SAFE KEY)
    if st.button(
        f"{icon} {title} - {direction_text}",
        key=f"card_{code}"
    ):
        st.session_state.direction = code
        st.rerun()

    # UI DISPLAY
    st.markdown(
        f"""
        <div style="
            padding:15px;
            border-radius:15px;
            border:2px solid {border};
            background-color:{background};
            text-align:center;
            margin-top:-10px;
        ">
            <h2>{title}</h2>
            <p style="color:#4F8EF7;">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------
# Main Page
# ---------------------------------------------------
def language_region_page():

    current = st.session_state.direction

    # =================================================
    # REGION SCREEN
    # =================================================
    if st.session_state.screen == "region":

        st.title("🌍 Select Language Region")

        if "region_direction" not in st.session_state:
            st.session_state.region_direction = ""

        if "region_time" not in st.session_state:
            st.session_state.region_time = time.time()

        if current != st.session_state.region_direction:
            st.session_state.region_direction = current
            st.session_state.region_time = time.time()

        elapsed = time.time() - st.session_state.region_time
        remaining = max(0, 2 - elapsed)

        st.info(f"⏳ Selecting Region in {remaining:.1f} sec")

        if elapsed >= 2:

            if current == "UP":
                st.session_state.region = "North"
            elif current == "RIGHT":
                st.session_state.region = "East"
            elif current == "LEFT":
                st.session_state.region = "West"
            elif current == "DOWN":
                st.session_state.region = "South"
            else:
                return

            st.session_state.screen = "language"
            st.rerun()

        # ---------- TOP ----------
        top = st.columns([1, 2, 1])
        with top[1]:
            selection_card("⬆️", "North", "North Region", "Look Up", "UP")

        # ---------- MIDDLE ----------
        left, center, right = st.columns([2, 1, 2])

        with left:
            selection_card("⬅️", "West", "West Region", "Look Left", "WEST")

        with center:
            st.markdown("<div class='eye-box'>👁</div>", unsafe_allow_html=True)

        with right:
            selection_card("➡️", "East", "East Region", "Look Right", "EAST")


        # ---------- BOTTOM ----------
        bottom = st.columns([1, 2, 1])
        with bottom[1]:
            selection_card("⬇️", "South", "South Region", "Look Down", "SOUTH")


    # =================================================
    # LANGUAGE SCREEN
    # =================================================
    elif st.session_state.screen == "language":

        st.title(f"🌐 {st.session_state.region} Languages")

        languages = REGIONS[st.session_state.region]

        if "language_direction" not in st.session_state:
            st.session_state.language_direction = ""

        if "language_time" not in st.session_state:
            st.session_state.language_time = time.time()

        if current != st.session_state.language_direction:
            st.session_state.language_direction = current
            st.session_state.language_time = time.time()

        elapsed = time.time() - st.session_state.language_time
        remaining = max(0, 2 - elapsed)

        st.info(f"⏳ Selecting Language in {remaining:.1f} sec")

        if elapsed >= 2:

            if current == "UP":
                st.session_state.language = languages[0]
            elif current == "RIGHT":
                st.session_state.language = languages[1]
            elif current == "LEFT":
                st.session_state.language = languages[2]
            elif current == "DOWN":
                st.session_state.language = languages[3]
            else:
                return

            st.session_state.language_selected = True
            st.session_state.screen = "dashboard"
            st.session_state.page = "menu"

            st.rerun()

        # ---------- TOP ----------
        top = st.columns([1, 2, 1])
        with top[1]:
            selection_card("⬆️", languages[0], languages[0], "Look Up", "UP")

        # ---------- MIDDLE ----------
        left, center, right = st.columns([2, 1, 2])

        with left:
           selection_card("⬅️", languages[2], languages[2], "Look Left", "LEFT")

        with center:
            st.markdown("<div class='eye-box'>👁</div>", unsafe_allow_html=True)

        with right:
            selection_card("➡️", languages[1], languages[1], "Look Right", "RIGHT")

        # ---------- BOTTOM ----------
        bottom = st.columns([1, 2, 1])
        with bottom[1]:
            selection_card("⬇️", languages[3], languages[3], "Look Down", "DOWN")