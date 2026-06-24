import streamlit as st
from ui.food import food_page
from ui.drink import drink_page
from ui.basic_needs import basic_page
from ui.emergency import emergency_page
from ui.snacks import snacks_page


def show_menu(direction):

    if direction == "menu":

        st.markdown("## Main Communication Menu")

        col1, col2, col3 = st.columns([1,2,1])

        with col2:
            if st.button("🚨 Emergency"):
                st.session_state.page = "emergency"
                st.rerun()

        left,right = st.columns(2)

        with left:
            if st.button("🍔 Food"):
                st.session_state.page = "food"
                st.rerun()

        with right:
            if st.button("🧑 Basic Needs"):
                st.session_state.page = "basic"
                st.rerun()

        col1,col2,col3 = st.columns([1,2,1])

        with col2:
            if st.button("🥤 Drink"):
                st.session_state.page = "drink"
                st.rerun()

    elif direction == "food":
        food_page()

    elif direction == "drink":
        drink_page()

    elif direction == "basic":
        basic_page()

    elif direction == "emergency":
        emergency_page()
    elif page == "snacks":
        snacks_page()