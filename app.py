import streamlit as st

st.set_page_config(
    page_title="GazeConnect",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------
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

# -----------------------------
# Styling
# -----------------------------

st.markdown("""
<style>

.main{
    background:#F7FAFF;
}

.title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#005792;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:20px;
}

div.stButton > button{
    width:100%;
    height:90px;
    font-size:22px;
    border-radius:20px;
    font-weight:bold;
}

.block{
    border:2px solid #E5E7EB;
    border-radius:18px;
    padding:15px;
    background:white;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">GazeConnect</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Affordable Eye Controlled Communication System</div>',
    unsafe_allow_html=True
)

# =====================================
# Camera + Status
# =====================================

def camera_panel():

    left, right = st.columns([2,1])

    with left:

        st.markdown("### 📷 Live Camera")

        st.image(
            "https://placehold.co/640x420?text=Live+Camera",
            use_container_width=True
        )

    with right:

        st.markdown("### Status")

        st.success(f"Language : {st.session_state.language}")

        st.info(f"Direction : {st.session_state.direction}")

        st.success(f"Gesture : {st.session_state.gesture}")

        st.warning("Selected Phrase")

        st.markdown(
            f"### {st.session_state.phrase}"
        )

# =====================================
# HOME
# =====================================

def home_page():

    top1, top2, top3 = st.columns([1,2,1])

    with top2:

        if st.button("🌐 LANGUAGE"):

            st.session_state.page="language"
            st.rerun()

    st.write("")

    left, center, right = st.columns([1.2,2,1.2])

    with left:

        if st.button("👨‍⚕️ HEALTH"):

            st.session_state.page="health"
            st.rerun()

    with center:

        camera_panel()

    with right:

        if st.button("🍽️ FOOD & DRINK"):

            st.session_state.page="food"
            st.rerun()

    st.write("")
    st.write("")

    c1,c2,c3=st.columns([1,2,1])

    with c2:

        if st.button("🆘 ASSISTANCE"):

            st.session_state.page="assist"
            st.rerun()
# =====================================
# HEALTH PAGE
# =====================================

def health_page():

    st.header("👨‍⚕️ Health")

    camera_panel()

    st.divider()

    c1, c2 = st.columns(2)

    with c1:
        if st.button("💊 Medicine"):
            st.session_state.phrase = "I need my medicine"

        if st.button("🤕 Pain"):
            st.session_state.phrase = "I am in pain"

    with c2:
        if st.button("🚨 Emergency"):
            st.session_state.phrase = "Emergency! Please help!"

        if st.button("👨‍⚕️ Call Doctor"):
            st.session_state.phrase = "Please call the doctor"


# =====================================
# FOOD PAGE
# =====================================

def food_page():

    st.header("🍽️ Food & Drink")

    camera_panel()

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        if st.button("🍛 Food"):
            st.session_state.phrase = "I am hungry"

        if st.button("🥤 Drinks"):
            st.session_state.phrase = "I need water"

    with c2:

        if st.button("🍎 Fruits"):
            st.session_state.phrase = "I want fruits"

        if st.button("🍪 Snacks"):
            st.session_state.phrase = "I want snacks"


# =====================================
# ASSISTANCE PAGE
# =====================================

def assist_page():

    st.header("🆘 Assistance")

    camera_panel()

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        if st.button("🚽 Washroom"):
            st.session_state.phrase = "I need the washroom"

        if st.button("😴 Sleep"):
            st.session_state.phrase = "I want to sleep"

    with c2:

        if st.button("🚶 Outing"):
            st.session_state.phrase = "Please take me outside"

        if st.button("🍽️ Hungry"):
            st.session_state.phrase = "I am hungry"


# =====================================
# LANGUAGE PAGE
# =====================================

def language_page():

    st.header("🌐 Language")

    camera_panel()

    st.divider()

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


# =====================================
# ROUTER
# =====================================

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

st.divider()

st.caption(
    "Developed using MediaPipe • OpenCV • Streamlit • gTTS"
)