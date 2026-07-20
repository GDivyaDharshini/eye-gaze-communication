import streamlit as st
from tracker import get_frame
def navigation_layout(title, left, right, bottom):

    st.markdown(
        f"""
        <div style="
        text-align:center;
        color:white;
        font-size:22px;
        font-weight:bold;
        margin-bottom:15px;">
        {title}
        </div>
        """,
        unsafe_allow_html=True
    )

    left_col, center_col, right_col = st.columns([1.2,3,1.2])

    with left_col:
        if st.button(left, use_container_width=True):
            st.session_state.page = "food"
            st.rerun()

    with center_col:
        camera_panel()

    with right_col:
        if st.button(right, use_container_width=True):
            st.session_state.page = "assist"
            st.rerun()

    st.write("")

    _, bottom_col, _ = st.columns([1,2,1])

    with bottom_col:
        if st.button(bottom, use_container_width=True):
            st.session_state.phrase = "Hello"
st.set_page_config(
    page_title="GazeConnect",
    layout="wide"
)

# =============================
# SESSION STATE
# =============================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "language" not in st.session_state:
    st.session_state.language = "English"

if "direction" not in st.session_state:
    st.session_state.direction = "CENTER"

if "gesture" not in st.session_state:
    st.session_state.gesture = "READY"

if "phrase" not in st.session_state:
    st.session_state.phrase = "Nothing Selected"

if "theme" not in st.session_state:
    st.session_state.theme = "dark"



# =============================
# CSS (BLUE DARK UI + FIT SCREEN)
# =============================
st.markdown("""
<style>

/* APP BACKGROUND */
.main {
    background: linear-gradient(135deg, #071a3a, #0b2a5e);
}

/* TITLE */
.title {
    text-align:center;
    font-size:25px;
    font-weight:bold;
    color:#4ea1ff;
}

.subtitle {
    text-align:center;
    color:#cbd5e1;
    margin-bottom:5px;
    font-size:14px;
}

/* BUTTONS SMALLER */
div.stButton > button {
    width:100%;
    height:75px;
    font-size:16px;
    border-radius:14px;
    font-weight:bold;
}

/* CAMERA BOX */
.camera {
    border-radius:16px;
    padding:10px;
    background:#0f1f3a;
    box-shadow:0px 4px 20px rgba(0,0,0,0.3);
}

/* STATUS BOX (VISIBLE NOW) */
.status-box {
    position: fixed;
    top: 70px;
    right: 15px;
    background: rgba(10, 20, 40, 0.95);
    color: white;
    padding: 12px;
    border-radius: 12px;
    width: 220px;
    font-size: 13px;
    z-index: 999;
    border: 1px solid #1e3a8a;
}

/* TOP TASKBAR */
.taskbar {
    display:flex;
    justify-content:center;
    gap:8px;
    margin-bottom:5px;
}

.taskbar button {
    padding:7px 12px;
    border-radius:10px;
    border:none;
    font-weight:bold;
    background:#1e3a8a;
    color:white;
    font-size:12px;
}

/* REMOVE SCROLL SPACE */
.block-container {
    padding-top: 0.8rem;
    padding-bottom: 0rem;
}

</style>
""", unsafe_allow_html=True)


# =============================
# HEADER
# =============================
col1, col2, col3 = st.columns([8,1,1])

with col1:
    st.markdown('<div class="title">GazeConnect</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Affordable Eye Controlled Communication System</div>', unsafe_allow_html=True)

with col3:
    st.button("🌙")




# =============================
# CAMERA
# =============================


def camera_panel():

    st.markdown("""
    <div class="camera">
        <h3 style="text-align:center;color:white;">
        🎥 Live Camera
        </h3>
    """, unsafe_allow_html=True)

    camera_placeholder = st.empty()

    frame = get_frame()

    if frame is not None:
        camera_placeholder.image(
            frame,
            use_container_width=True
        )
    else:
        camera_placeholder.warning("Unable to access camera.")

   
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown(f"""
<div style="
margin-top:10px;
background:#14284d;
padding:10px;
border-radius:10px;
text-align:center;
color:white;
">
💬 {st.session_state.phrase}
</div>
""", unsafe_allow_html=True)
# =============================
# STATUS BOX
# =============================
st.markdown(f"""
<div class="status-box">
<b>👁 STATUS</b><br><br>
Language: {st.session_state.language}<br>
Direction: {st.session_state.direction}<br>
Gesture: {st.session_state.gesture}<br>
Phrase: {st.session_state.phrase}
</div>
""", unsafe_allow_html=True)


# =============================
# HOME PAGE
# =============================
def home_page():

    navigation_layout(
        "⬆️ Basic Needs",
        "🍽 Food",
        "🚨 Emergency",
        "💬 Common Phrases"
    )
    
# =============================
# PAGES (SAME LOGIC)
# =============================
def health_page():
    st.header("Health")
    camera_panel()

    c1, c2 = st.columns(2)

    with c1:
        if st.button("💊 Medicine"):
            st.session_state.phrase = "Need medicine"
        if st.button("🤕 Pain"):
            st.session_state.phrase = "I am in pain"

    with c2:
        if st.button("🚨 Emergency"):
            st.session_state.phrase = "Emergency help!"
        if st.button("👨‍⚕️ Doctor"):
            st.session_state.phrase = "Call doctor"


def food_page():

    navigation_layout(
        "🥤 Drinks",
        "🥗 Veg",
        "🍗 Non-Veg",
        "🍟 Snacks"
    )
def assist_page():
    st.header("Assistance")
    camera_panel()

    c1, c2 = st.columns(2)

    with c1:
        if st.button("🚽 Washroom"):
            st.session_state.phrase = "Need washroom"
        if st.button("😴 Sleep"):
            st.session_state.phrase = "I want sleep"

    with c2:
        if st.button("🚶 Outside"):
            st.session_state.phrase = "Take me outside"
        if st.button("🍽 Hungry"):
            st.session_state.phrase = "I am hungry"


def language_page():
    st.header("Language")
    camera_panel()

    c1, c2 = st.columns(2)

    with c1:
        if st.button("English"):
            st.session_state.language = "English"
        if st.button("தமிழ்"):
            st.session_state.language = "Tamil"

    with c2:
        if st.button("हिन्दी"):
            st.session_state.language = "Hindi"
        if st.button("বাংলা"):
            st.session_state.language = "Bengali"


# =============================
# ROUTER
# =============================
page = st.session_state.page

if page == "home":
    home_page()
elif page == "health":
    health_page()
elif page == "food":
    food_page()
elif page == "assist":
    assist_page()
elif page == "language":
    language_page()


st.markdown("<br>", unsafe_allow_html=True)
st.caption("GazeConnect • Streamlit Prototype • Hackathon UI")