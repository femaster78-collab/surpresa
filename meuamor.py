import streamlit as st
import random

# Configuração da página web fofa
st.set_page_config(page_title="💝 Surpresa!", page_icon="💖", layout="centered")

# Força o estilo do fundo rosa e esconde menus feios
st.markdown("""
    <style>
    .stApp { background-color: #fdf2f8 !important; }
    .stButton>button { width: 100% !important; font-weight: bold !important; height: 50px !important; }
    </style>
""", unsafe_allow_html=True)

# Inicializa as variáveis na memória da página
if "pos_nao" not in st.session_state:
    st.session_state.pos_nao = 0  
if "provocacao" not in st.session_state:
    st.session_state.provocacao = ""
if "aceitou" not in st.session_state:
    st.session_state.aceitou = False

# As 3 risadas puras que você pediu
risadas = ["Mwahahah! 😈", "Hihihihi! 🏃‍♀️", "Nyehehe! ☠️"]

def fugir():
    # Sorteia um número de 1 a 6 para mudar o botão de lugar drasticamente
    st.session_state.pos_nao = random.randint(1, 6) 
    st.session_state.provocacao = random.choice(risadas)

def clicar_sim():
    st.session_state.aceitou = True

# TELA FINAL (Se ela aceitar)
if st.session_state.aceitou:
    st.markdown("<h1 style='color: #be185d !important; text-align: center; font-family: Arial; font-size: 38px; margin-top: 80px;'>✨ 🎉 Sabia! 🎉 ✨</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #db2777 !important; text-align: center; font-family: Arial; font-size: 28px; margin-top: 20px;'>❤️ AMO VOCÊ! ❤️</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #4c0519 !important; text-align: center; font-family: Arial; font-size: 20px; margin-top: 20px;'>🥰 Não tinha como fugir!</h3>", unsafe_allow_html=True)
else:
    # TELA PRINCIPAL (Texto escuro forçado em HTML para não bugar no modo escuro)
    st.markdown("<h1 style='color: #4c0519 !important; text-align: center; font-family: Arial; font-size: 34px; margin-top: 40px;'>Você me ama? 🥺👉👈</h1>", unsafe_allow_html=True)
    
    if st.session_state.provocacao:
        st.markdown(f"<h3 style='color: #be185d !important; text-align: center; font-family: Courier New; font-size: 24px; margin-top: 10px;'>✨ {st.session_state.provocacao}</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Criando 4 colunas largas para o botão pular bem longe
    col1, col2, col3, col4 = st.columns(4)
    
    # O botão SIM fica travado na primeira coluna
    with col1:
        st.button("SIM! 😍", on_click=clicar_sim, type="primary")
        
    # O botão NÃO muda de lugar entre as colunas a cada toque dela
    if st.session_state.pos_nao == 0:
        with col3: st.button("Não 😭", on_click=fugir)
    elif st.session_state.pos_nao == 1:
        with col2: st.button("Não 😭", on_click=fugir)
    elif st.session_state.pos_nao == 2:
        with col4: st.button("Não 😭", on_click=fugir)
    elif st.session_state.pos_nao == 3:
        with col1: st.button("Não 😭", on_click=fugir)  # Pula pra baixo do SIM!
    elif st.session_state.pos_nao == 4:
        with col2: st.button("Não 😭", on_click=fugir)
    else:
        st.session_state.pos_nao = 0
        with col3: st.button("Não 😭", on_click=fugir)
