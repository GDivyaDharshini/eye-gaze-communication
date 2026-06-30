import streamlit as st
import time

from ui.food import food_page
from ui.drink import drink_page
from ui.basic_needs import basic_needs_page
from ui.emergency import emergency_page
from ui.snacks import snacks_page
from ui.confirmation import confirmation_page
from ui.dashboard_languages import dashboard_languages


# ---------------------------------------
# Card
# ---------------------------------------
def card(icon, title, direction, active=False):

    border = "#4F8EF7" if active else "#E8EEF8"
    background = "#EEF5FF" if active else "white"

    st.markdown(
        f"""
        <div style="
            background:{background};
            border:3px solid {border};
            border-radius:22px;
            padding:30px;
            text-align:center;
            box-shadow:0 8px 25px rgba(0,0,0,.08);
            margin-bottom:15px;
        ">

            <div style="font-size:60px;">
                {icon}
            </div>

            <div style="
                font-size:28px;
                font-weight:bold;
                color:#2E3A59;
                margin-top:10px;
            ">
                {title}
            </div>

            <div style="
                font-size:18px;
                color:#5B7FFF;
                margin-top:8px;
            ">
                {direction}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------
# Home Menu
# ---------------------------------------
def show_menu():

    current_direction = st.session_state.direction

    lang = dashboard_languages[st.session_state.language]

    # ---------------- Auto Selection Timer ----------------

    if "last_direction" not in st.session_state:
        st.session_state.last_direction = ""

    if "direction_time" not in st.session_state:
        st.session_state.direction_time = time.time()

    if current_direction != st.session_state.last_direction:

        st.session_state.last_direction = current_direction
        st.session_state.direction_time = time.time()

    elapsed = time.time() - st.session_state.direction_time
    remaining = max(0, 2 - elapsed)

    st.info(f"⏳ Auto Select in: {remaining:.1f} seconds")

    # ---------------- Eye Gaze Auto Selection ----------------

    if elapsed >= 2:

        if current_direction == "UP":
            st.session_state.page = "food"

        elif current_direction == "LEFT":
            st.session_state.page = "drink"

        elif current_direction == "RIGHT":
            st.session_state.page = "basic_needs"

        elif current_direction == "DOWN":
            st.session_state.page = "emergency"

        st.rerun()

    # ---------------- TOP ----------------

    top = st.columns([1, 2, 1])

    with top[1]:

        card(
            "🍔",
            lang["FOOD"],
            "↑ Look Up",
            active=current_direction == "UP"
        )

        if st.button("Select Food", use_container_width=True):

            st.session_state.page = "food"
            st.rerun()

    # ---------------- MIDDLE ----------------

    left, center, right = st.columns([2, 1, 2])

    with left:

        card(
            "🥤",
            lang["DRINKS"],
            "◀ Look Left",
            active=current_direction == "LEFT"
        )

        if st.button("Select Drinks", use_container_width=True):

            st.session_state.page = "drink"
            st.rerun()

    with center:

        st.markdown(
            """
            <div class="eye-box">
                👁
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        card(
            "🛏",
            lang["BASIC_NEEDS"],
            "Look Right ▶",
            active=current_direction == "RIGHT"
        )

        if st.button("Select Basic Needs", use_container_width=True):

            st.session_state.page = "basic_needs"
            st.rerun()

    # ---------------- BOTTOM ----------------

    bottom = st.columns([1, 2, 1])

    with bottom[1]:

        card(
            "🚨",
            lang["EMERGENCY"],
            "↓ Look Down",
            active=current_direction == "DOWN"
        )

        if st.button("Select Emergency", use_container_width=True):

            st.session_state.page = "emergency"
            st.rerun()


# ---------------------------------------
# Page Router
# ---------------------------------------
def page_router():

    page = st.session_state.page

    if page == "food":
        food_page()

    elif page == "drink":
        drink_page()

    elif page == "basic_needs":
        basic_needs_page()

    elif page == "emergency":
        emergency_page()

    elif page == "snacks":
        snacks_page()

    elif page == "confirmation":
        confirmation_page()