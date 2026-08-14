import streamlit as st
import random

st.set_page_config(page_title="💝 Uma surpresa para você!", page_icon="💖", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #fdf2f8; }
    h1 { color: #9d174d; text-align: center; font-family: 'Arial'; }
    .stButton>button { width: 100%; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("Você me ama? 🥺👉👈")

if "pos_nao" not in st.session_state: st.session_state.pos_nao = 0  
if "provocacao" not in st.session_state: st.session_state.provocacao = ""
if "aceitou" not in st.session_state: st.session_state.aceitou = False

risadas = ["Mwahahah! 😈", "Hihihihi! 🏃‍♀️", "Nyehehe! ☠️"]

def fugir():
    st.session_state.pos_nao = random.randint(1, 4) 
    st.session_state.provocacao = random.choice(risadas)

if st.session_state.aceitou:
    st.markdown("<h1 style='color: #be185d; margin-top: 50px;'>✨ 🎉 Sabia! 🎉 ✨<br><br>❤️ AMO VOCÊ! ❤️<br><br>🥰 Não tinha como fugir!</h1>", unsafe_allow_html=True)
else:
    if st.session_state.provocacao: st.subheader(f"✨ {st.session_state.provocacao}")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.button("SIM, MUITO! 😍", on_click=lambda: st.session_state.update({"aceitou": True}), type="primary")
    if st.session_state.pos_nao == 0:
        with col3: st.button("Não 😭", on_click=fugir)
    elif st.session_state.pos_nao == 1:
        with col2: st.button("Não 😭", on_click=fugir)
    elif st.session_state.pos_nao == 2:
        with col4: st.button("Não 😭", on_click=fugir)
    elif st.session_state.pos_nao == 3: st.session_state.pos_nao = 0
