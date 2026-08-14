import streamlit as st

st.set_page_config(page_title="💝 Surpresa!", page_icon="💖", layout="centered")

# 🦾 O SUPREMO CÓDIGO HÍBRIDO (Python + JavaScript Nativo para celular)
st.markdown("""
    <style>
    /* Força o fundo rosa e texto escuro em qualquer celular */
    html, body, .stApp { 
        background-color: #fdf2f8 !important; 
        color: #4c0519 !important;
        font-family: 'Arial', sans-serif !important;
    }
    
    .container {
        text-align: center;
        margin-top: 50px;
        position: relative;
        height: 500px;
        width: 100%;
    }
    
    .titulo {
        font-size: 30px;
        font-weight: bold;
        color: #9d174d !important;
        margin-bottom: 20px;
    }
    
    .risada {
        font-size: 22px;
        font-weight: bold;
        color: #db2777 !important;
        height: 40px;
        margin-bottom: 30px;
    }
    
    /* Estilo dos botões */
    .btn-comum {
        padding: 15px 30px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 12px;
        border: none;
        color: white !important;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
    }
    
    #btn-sim {
        background-color: #f472b6;
        position: absolute;
        left: 15%;
        top: 180px;
        width: 130px;
    }
    
    /* O NÃO começa na direita e muda para posição absoluta pelo JavaScript */
    #btn-nao {
        background-color: #64748b;
        position: absolute;
        left: 55%;
        top: 180px;
        width: 100px;
        transition: all 0.1s ease; /* Efeito suave de movimento */
    }
    </style>

    <div class="container" id="painel-jogo">
        <div class="titulo">Você me ama? 🥺👉👈</div>
        <div class="risada" id="texto-risada"></div>
        
        <button class="btn-comum" id="btn-sim" onclick="ganhou()">SIM! 😍</button>
        <button class="btn-comum" id="btn-nao" onmouseenter="fugir()" ontouchstart="fugir()">Não 😭</button>
    </div>

    <script>
    // Banco de dados de risadas direto no navegador
    const risadas = ["Mwahahah! 😈", "Hihihihi! 🏃‍♀️", "Nyehehe! ☠️"];
    
    function fugir() {
        const btnNao = document.getElementById('btn-nao');
        const txtRisada = document.getElementById('texto-risada');
        
        // Sorteia pixels reais baseados no tamanho da tela do celular dela
        const novoX = Math.floor(Math.random() * 70) + 5; // Entre 5% e 75% da largura
        const novoY = Math.floor(Math.random() * 250) + 120; // Entre 120px e 370px de altura
        
        // Aplica a nova posição instantaneamente (Zero delay de internet!)
        btnNao.style.left = novoX + '%';
        btnNao.style.top = novoY + 'px';
        
        // Sorteia a risada
        const risadaAleatoria = risadas[Math.floor(Math.random() * risadas.length)];
        txtRisada.innerText = "✨ " + risadaAleatoria;
    }
    
    function ganhou() {
        const painel = document.getElementById('painel-jogo');
        // Transforma a tela inteira na mensagem de amor
        painel.innerHTML = `
            <div style="margin-top: 80px; text-align: center; animation: fadeIn 0.5s;">
                <h1 style="color: #be185d !important; font-size: 36px; font-weight: bold; font-family: Arial;">✨ 🎉 Sabia! 🎉 ✨</h1>
                <h2 style="color: #db2777 !important; margin-top: 20px; font-family: Arial;">❤️ AMO VOCÊ! ❤️</h2>
                <h3 style="color: #4c0519 !important; font-size: 18px; margin-top: 20px; font-family: Arial;">Anão tinha como fugir! 🥰</h3>
            </div>
        `;
    }
    </script>
""", unsafe_allow_html=True)
