import streamlit as st
import random

# Configuração da página mobile
st.set_page_config(page_title="💝 Surpresa!", page_icon="💖", layout="centered")

# Cores travadas contra modo escuro usando CSS interno do Streamlit
st.markdown("""
    <style>
    /* Força o fundo rosa bebê */
    .stApp { background-color: #fdf2f8 !important; }
    
    /* Força os títulos a ficarem em rosa escuro/vinho bem nítidos */
    h1, h2, h3, p, span, .stMarkdown { 
        color: #4c0519 !important; 
        text-align: center !important; 
        font-family: 'Arial', sans-serif !important;
    }
    
    /* Customização dos botões para ficarem fofos no celular */
    .stButton>button {
        width: 100% !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        height: 55px !important;
        font-size: 16px !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializa as variáveis na memória da página
if "pos_nao" not in st.session_state:
    st.session_state.pos_nao = 0  
if "provocacao" not in st.session_state:
    st.session_state.provocacao = ""
if "aceitou" not in st.session_state:
    st.session_state.aceitou = False

# As 3 risadas que você escolheu
risadas = ["Mwahahah! 😈", "Hihihihi! 🏃‍♀️", "Nyehehe! ☠️"]

def fugir():
    # Sorteia uma das 4 colunas para o botão reaparecer instantaneamente
    st.session_state.pos_nao = random.randint(1, 4) 
    st.session_state.provocacao = random.choice(risadas)

def clicar_sim():
    st.session_state.aceitou = True

# LÓGICA DE TELAS
if st.session_state.aceitou:
    st.markdown("<h1 style='font-size: 36px; margin-top: 50px;'>✨ 🎉 Sabia! 🎉 ✨</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #db2777 !important;'>❤️ AMO VOCÊ! ❤️</h2>", unsafe_allow_html=True)
    st.markdown("<h3>🥰 Não tinha como fugir!</h3>", unsafe_allow_html=True)
else:
    st.markdown("<h1>Você me ama? 🥺👉👈</h1>", unsafe_allow_html=True)
    
    # Mostra a risada de provocação centralizada
    if st.session_state.provocacao:
        st.markdown(f"<h3>✨ {st.session_state.provocacao}</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Cria as 4 colunas perfeitas para o celular
    col1, col2, col3, col4 = st.columns(4)
    
    # O botão SIM fica estático e destacado na primeira coluna
    with col1:
        st.button("SIM! 😍", on_click=clicar_sim, type="primary")
        
    # O botão NÃO fica pulando de coluna em coluna a cada toque!
    if st.session_state.pos_nao == 0:
        with col3: st.button("Não 😭", on_click=fugir)
    elif st.session_state.pos_nao == 1:
        with col2: st.button("Não 😭", on_click=fugir)
    elif st.session_state.pos_nao == 2:
        with col4: st.button("Não 😭", on_click=fugir)
    elif st.session_state.pos_nao == 3:
        # Posição bônus: ele volta para o estado inicial para continuar o ciclo infinito
        st.session_state.pos_nao = 0
        with col3: st.button("Não 😭", on_click=fugir)
