import streamlit as st

def emergency_page():

    st.header("🚨 Emergency")

    st.error("⚠️ Emergency Communication")

    # UP
    top = st.columns([1,2,1])

    with top[1]:
        if st.button("👨‍⚕️ Call Caregiver"):
            st.session_state.message = "Call Caregiver Immediately"

    # LEFT - CENTER - RIGHT
    middle = st.columns(3)

    with middle[0]:
        if st.button("🆘 Help Now"):
            st.session_state.message = "I Need Help Immediately"

    with middle[1]:
        st.error("👁️ LOOK HERE")

    with middle[2]:
        if st.button("🏥 Medical Emergency"):
            st.session_state.message = "Medical Emergency"

    # DOWN
    bottom = st.columns([1,2,1])

    with bottom[1]:
        if st.button("📢 Send Alert"):
            st.session_state.message = "Emergency Alert Sent"

    # Back Button
    if st.button("⬅ Back"):
        st.session_state.page = "menu"
        st.rerun()