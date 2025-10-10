# ==============================
# 🌸 Programa Saúde da Fe 🌸 
# ==============================

import streamlit as st
from pathlib import Path
import random

# ---------- LIMPAR CACHE ----------
st.cache_data.clear()

# ---------- CONFIGURAÇÃO ----------
st.set_page_config(page_title="Programa Saúde da FE", page_icon="💖", layout="centered")

# ---------- ESTILO ----------
st.markdown("""
<style>
.small-muted { color:#777; font-size:0.9rem; }
.card { padding:1rem; border-radius:12px; background:#fafafa; border:1px solid #eee; }
.stVideo {border-radius: 16px; box-shadow: 0px 0px 12px rgba(0,0,0,0.1);}
</style>
""", unsafe_allow_html=True)

# ---------- TÍTULO ----------
st.title("🌸 Programa Saúde da FE")
st.markdown("_Cuidar do corpo é um ato de amor-próprio._ 💕")
st.subheader("Calculadora de IMC, Água, Exercício e Peso Ideal")
st.write("Preencha seus dados e veja suas recomendações personalizadas. 🌿")

# ---------- FUNÇÕES ----------
def calcular_imc(peso: float, altura: float) -> float:
    if altura <= 0: return 0
    return peso / (altura ** 2)

def classificar_imc(imc: float) -> str:
    if imc < 18.5: return "Abaixo do peso"
    elif imc < 25: return "Peso adequado"
    elif imc < 30: return "Sobrepeso"
    elif imc < 35: return "Obesidade grau I"
    elif imc < 40: return "Obesidade grau II"
    else: return "Obesidade grau III"

def calcular_agua_diaria(peso: float) -> int:
    return int(peso * 35)

def calcular_exercicio(imc: float) -> str:
    if imc < 25:
        return "30 minutos/dia (5x por semana)"
    elif imc < 30:
        return "45 minutos/dia (5–6x por semana)"
    else:
        return "60 minutos/dia (6x por semana)"

def calcular_peso_ideal(altura: float, sexo: str) -> float:
    altura_cm = altura * 100
    polegadas = altura_cm / 2.54
    if sexo.upper() == "M":
        return 50 + 2.3 * (polegadas - 60)
    return 45.5 + 2.3 * (polegadas - 60)

def frase_motivacional(nome: str, classe: str) -> str:
    frases = [
        "É se amando que tudo se transforma. 💫",
        "Seu corpo é sua casa: trate-o com carinho. 🌿",
        "Pequenos passos diários geram grandes mudanças. ✨",
        "Você merece cuidado, presença e gentileza. 💖",
        "Beber água é um abraço por dentro. 💧"
    ]
    base = random.choice(frases)
    return f"{nome}, {base}" if nome else base

# ---------- FORMULÁRIO ----------
with st.form("form_saude"):
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome")
        idade = st.number_input("Idade", 0, 120, 30)
        sexo = st.selectbox("Sexo", ["F", "M"])
    with col2:
        altura = st.number_input("Altura (m)", 0.0, 2.30, 1.65, step=0.01)
        peso = st.number_input("Peso (kg)", 0.0, 300.0, 65.0, step=0.1)

    enviar = st.form_submit_button("Calcular ✅")

# ---------- RESULTADOS ----------
if enviar:
    imc = calcular_imc(peso, altura)
    classe = classificar_imc(imc)
    agua = calcular_agua_diaria(peso)
    exercicio = calcular_exercicio(imc)
    ideal = calcular_peso_ideal(altura, sexo)
    frase = frase_motivacional(nome.strip() if nome else None, classe)

    st.markdown("---")
    st.markdown("### 📊 Resultados")
    c1, c2, c3 = st.columns(3)
    c1.metric("IMC", f"{imc:.2f}", classe)
    c2.metric("Água/dia", f"{agua} ml")
    c3.metric("Peso ideal", f"{ideal:.1f} kg")

    st.markdown("### 🏃 Recomendação de exercício")
    st.write(exercicio)

    st.markdown("### 💖 Mensagem motivacional")
    st.success(frase)

# ===================== VÍDEO MOTIVACIONAL =====================
from pathlib import Path

st.markdown("### 🎬 É se amando que tudo se transforma ✨")

# Ajuste estes dois nomes de acordo com o seu repositório:
BRANCH = "principal"  # use "main" se for o seu caso
VIDEO_FILENAME = "video_amor_proprio.mp4"  # troque se o seu arquivo for "video_amor_proprio1.mp4"

# 1) Tenta tocar a partir do arquivo local no repositório (mais confiável)
video_path = Path(VIDEO_FILENAME)
if video_path.exists():
    st.video(str(video_path))
else:
    # 2) Se não estiver local, usa o RAW do GitHub
    RAW_LINK = f"https://raw.githubusercontent.com/rosalva1911-eng/programa-saude-fe/{BRANCH}/{VIDEO_FILENAME}"
    st.video(RAW_LINK)

st.caption("💫 O primeiro passo para cuidar do corpo é cuidar do coração.")

# ---------- RODAPÉ ----------
st.markdown("---")
st.markdown('<p class="small-muted">Programa Saúde da FE • Feito com carinho em Streamlit 🌸</p>', unsafe_allow_html=True)

