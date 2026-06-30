import streamlit as st


# ---------------------------------------
# Direction Card
# ---------------------------------------
def direction_card(icon, title, direction, active=False):

    border = "#4F8EF7" if active else "#E8EEF8"
    background = "#EEF5FF" if active else "white"

    st.markdown(
        f"""
        <div style="
            background:{background};
            border:3px solid {border};
            border-radius:22px;
            padding:28px;
            text-align:center;
            box-shadow:0 8px 25px rgba(0,0,0,.08);
            min-height:180px;
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
                color:#5B7FFF;
                font-size:18px;
                margin-top:8px;
            ">
                {direction}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------
# Page Title
# ---------------------------------------
def page_title(title):

    st.markdown(
        f"""
        <h1 style="
            text-align:center;
            color:#2E3A59;
            margin-bottom:25px;
        ">
            {title}
        </h1>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------
# Back Button
# ---------------------------------------
def back_button(page="menu"):

    if st.button("⬅ Back", use_container_width=True):

        st.session_state.page = page
        st.rerun()