import streamlit as st

from ui.menu import show_menu, page_router
from ui.styles import load_css
from ui.language_region import language_region_page
from ui.dashboard_languages import dashboard_languages
from utils.speech import speak

# =================================================
# PAGE CONFIG
# =================================================
st.set_page_config(
    page_title="GazeConnect",
    page_icon="👁️",
    layout="wide"
)

load_css()

# =================================================
# SESSION STATE (MERGED)
# =================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "screen" not in st.session_state:
    st.session_state.screen = "region"

if "language" not in st.session_state:
    st.session_state.language = "English"

if "message" not in st.session_state:
    st.session_state.message = "---"

if "direction" not in st.session_state:
    st.session_state.direction = "Waiting..."

if "region" not in st.session_state:
    st.session_state.region = ""

if "language_selected" not in st.session_state:
    st.session_state.language_selected = False

if "selected_item" not in st.session_state:
    st.session_state.selected_item = ""

# =================================================
# LANGUAGE DATA
# =================================================
lang = dashboard_languages.get(
    st.session_state.language,
    dashboard_languages["English"]
)

# =================================================
# SIDEBAR
# =================================================
with st.sidebar:
    st.title("⚙️ Settings")

    st.write("Current Language")
    st.success(f"🌐 {st.session_state.language}")

    if st.button("🔄 Change Language"):
        st.session_state.screen = "region"
        st.session_state.region = ""
        st.session_state.language_selected = False
        st.rerun()

# =================================================
# HEADER
# =================================================
left, right = st.columns([5, 1])

with left:
    st.markdown(
        '<div class="title">GazeConnect</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Affordable Eye-Controlled Communication System</div>',
        unsafe_allow_html=True
    )

# =================================================
# OUTPUT SECTION
# =================================================
st.markdown(f"## 🗣️ {lang['OUTPUT']}")

message = st.session_state.message
if message == "---":
    message = lang["LOOK"]

st.markdown(
    f"""
    <div class="message-box">
        💬 {message}
    </div>
    """,
    unsafe_allow_html=True
)

# =================================================
# SPEAK BUTTON
# =================================================
if st.button("🔊 Speak", use_container_width=True):
    if st.session_state.message != "---":
        speak(st.session_state.message)

st.divider()

# =================================================
# EYE DIRECTION TEST
# =================================================
st.session_state.direction = st.selectbox(
    "👀 Test Eye Direction",
    ["Waiting...", "UP", "LEFT", "RIGHT", "DOWN"]
)

direction = st.session_state.direction

st.markdown("### 👀 Gaze Direction")

if direction == "UP":
    st.success("⬆️ Looking Up")
elif direction == "LEFT":
    st.success("⬅️ Looking Left")
elif direction == "RIGHT":
    st.success("➡️ Looking Right")
elif direction == "DOWN":
    st.success("⬇️ Looking Down")
else:
    st.info("👁 Waiting for Eye Movement...")

# =================================================
# MAIN FLOW
# =================================================
if st.session_state.screen in ["region", "language"]:
    language_region_page()

elif st.session_state.screen == "dashboard":

    if st.session_state.page == "menu":
        show_menu()
    else:
        page_router()

st.divider()

# =================================================
# HEAD GESTURE STATUS
# =================================================
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.success(f" {lang['YES']}")

with col2:
    st.info(f"👤 {lang['HEAD']} : {lang['WAITING']}")

with col3:
    st.error(f" {lang['NO']}")