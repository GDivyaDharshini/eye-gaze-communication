import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .main{
        background:#F7F9FC;
    }

    .title{
        font-size:46px;
        font-weight:800;
        color:#2E2A5E;
    }

    .subtitle{
        color:#7B7B92;
        font-size:18px;
        margin-top:-10px;
        margin-bottom:25px;
    }

    .message-box{
        background:#EEF6FF;
        padding:20px;
        border-radius:15px;
        font-size:24px;
        font-weight:600;
        border:1px solid #D5E6FF;
    }

    .gesture{
        padding:18px;
        border-radius:15px;
        text-align:center;
        font-size:22px;
        font-weight:600;
    }
    .card{
    background:white;
    border-radius:20px;
    padding:25px;
    text-align:center;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
    border:1px solid #E6ECF5;
    min-height:150px;
    transition:0.3s;
}

.card:hover{
    transform:scale(1.03);
    box-shadow:0px 8px 20px rgba(0,0,0,0.15);
}

.card-title{
    font-size:24px;
    font-weight:bold;
    color:#2E3A59;
}

.card-icon{
    font-size:50px;
}

.card-direction{
    color:#5B7FFF;
    font-size:18px;
    margin-top:10px;
}
.direction-card{
background:white;
padding:30px;
border-radius:22px;
text-align:center;
box-shadow:0px 8px 25px rgba(0,0,0,.08);
border:1px solid #E8EEF8;
transition:.3s;
cursor:pointer;
margin-bottom:15px;
}
.direction-card:hover{
transform:translateY(-5px);
box-shadow:0px 15px 30px rgba(91,127,255,.25);
}

.direction-icon{
font-size:60px;
margin-bottom:12px;
}

.direction-title{
font-size:28px;
font-weight:700;
color:#2E3A59;
}
.direction-text{
font-size:18px;
color:#5B7FFF;
margin-top:8px;
}

.eye-box{
background:#FFF7DD;
height:170px;
border-radius:22px;
display:flex;
align-items:center;
justify-content:center;
font-size:80px;
border:3px dashed #FFD25E;
}
.food-card{
    background:#FFFFFF;
    border-radius:22px;
    padding:25px;
    text-align:center;
    border:1px solid #E5EAF5;
    box-shadow:0 6px 18px rgba(0,0,0,.08);
    transition:.3s;
    min-height:180px;
}

.food-card:hover{
    transform:translateY(-5px);
    box-shadow:0 12px 28px rgba(0,0,0,.15);
}

.food-icon{
    font-size:60px;
}

.food-title{
    font-size:30px;
    font-weight:700;
    margin-top:10px;
    color:#2E3A59;
}

.food-direction{
    font-size:18px;
    color:#5B7FFF;
    margin-top:10px;
}

.eye-center{
    height:220px;
    background:#FFF8DD;
    border-radius:22px;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:90px;
    border:3px dashed #FFD55A;
}

.back-btn{
    margin-top:20px;
}
/* Buttons */
div.stButton > button {
    width:100%;
    height:55px;
    border-radius:15px;
    font-size:18px;
    font-weight:600;
    border:none;
    background:#4F8EF7;
    color:white;
    transition:0.3s;
}

div.stButton > button:hover{
    background:#2F6CE5;
    transform:translateY(-2px);
}
    </style>
    """, unsafe_allow_html=True)