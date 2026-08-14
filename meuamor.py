import streamlit as st
import random

# Configuração da página mobile
st.set_page_config(page_title="💝 Surpresa!", page_icon="💖", layout="centered")

# Inicializa as variáveis na memória
if "x" not in st.session_state: st.session_state.x = 50
if "y" not in st.session_state: st.session_state.y = 250
if "risada" not in st.session_state: st.session_state.risada = ""
if "ganhou" not in st.session_state: st.session_state.ganhou = False

risadas = ["Mwahahah! 😈", "Hihihihi! 🏃‍♀️", "Nyehehe! ☠️"]

def fugir():
    # Sorteia coordenadas de pixels reais para sumir e brotar em qualquer canto
    st.session_state.x = random.randint(10, 80)
    st.session_state.y = random.randint(180, 400)
    st.session_state.risada = random.choice(risadas)

# 🎨 DESIGN PREMIUM MOBILE (Força cores vibrantes e fixa posições)
st.markdown(f"""
    <style>
    .stApp {{ background-color: #fdf2f8 !important; }}
    .titulo {{ color: #9d174d !important; text-align: center; font-family: 'Arial'; font-size: 32px; font-weight: bold; margin-bottom: 20px; }}
    .risada {{ color: #db2777 !important; text-align: center; font-family: 'Courier New'; font-size: 22px; font-weight: bold; height: 30px; margin-bottom: 30px; }}
    
    /* Força o botão SIM a ficar grande e fixo */
    .btn-sim {{ position: absolute; left: 15%; top: 250px; width: 140px; }}
    .btn-sim button {{ background-color: #f472b6 !important; color: white !important; font-size: 16px !important; border-radius: 10px !important; border: none !important; height: 50px; }}
    
    /* Força o botão NÃO a flutuar de forma caótica em pixels na tela */
    .btn-nao {{ position: absolute; left: {st.session_state.x}%; top: {st.session_state.y}px; width: 100px; z-index: 999; }}
    .btn-nao button {{ background-color: #94a3b8 !important; color: white !important; font-size: 16px !important; border-radius: 10px !important; border: none !important; height: 50px; }}
    </style>
""", unsafe_allow_html=True)

# Desenha os textos com contraste blindado contra o tema escuro
if st.session_state.ganhou:
    st.markdown("<div style='margin-top: 100px; text-align: center;'><h1 style='color: #be185d !important; font-size: 36px; font-weight: bold;'>✨ 🎉 Sabia! 🎉 ✨</h1><h2 style='color: #db2777 !important; margin-top: 20px;'>❤️ AMO VOCÊ! ❤️</h2><p style='color: #9d174d !important; font-size: 18px; margin-top: 20px;'>🥰 Não tinha como fugir!</p></div>", unsafe_allow_html=True)
else:
    st.markdown('<div class="titulo">Você me ama? 🥺👉👈</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="risada">{st.session_state.risada}</div>', unsafe_allow_html=True)
    
    # Renderiza os botões usando as classes CSS absolutas
    st.markdown('<div class="btn-sim">', unsafe_allow_html=True)
    st.button("SIM, MUITO! 😍", on_click=lambda: st.session_state.update({"ganhou": True}))
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="btn-nao">', unsafe_allow_html=True)
    st.button("Não 😭", on_click=fugir)
    st.markdown('</div>', unsafe_allow_html=True)
