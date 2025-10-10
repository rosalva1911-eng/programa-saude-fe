import streamlit as st

# ===================== CONFIG =====================
st.set_page_config(page_title="Programa Saúde da Fê 💧", page_icon="🌿", layout="centered")
st.title("🌸 Programa Saúde da Fê")
st.subheader("Calculadora de IMC, Água, Exercício e Peso Ideal")

st.write("Preencha seus dados e veja suas recomendações personalizadas. 💪🍃")
import streamlit as st

# ===================== CONFIG =====================
st.set_page_config(page_title="Programa Saúde da Fê 💧", page_icon="💖")
st.title("🌸 Programa Saúde da Fê")
st.subheader("Calculadora de IMC, Água, Exercício e Peso Ideal")
st.write("Preencha seus dados e veja suas recomendações personalizadas!")

# --- vídeo motivacional direto do HeyGen ---
st.markdown("### 🎬 Amor-próprio em 20 segundos")
st.video("https://app.heygen.com/videos/eb44f76d34604cd7b672b7b4d32e602c")
st.caption("É se amando que tudo se transforma. 💫")

# ===================== FUNÇÕES =====================
def calcular_imc(peso: float, altura: float) -> float:
    if altura <= 0:
        return 0.0
    return peso / (altura ** 2)
# ===================== FUNÇÕES =====================
def calcular_imc(peso: float, altura: float) -> float:
    if altura <= 0:
        return 0.0
    return peso / (altura ** 2)

def classificar_imc(imc: float) -> str:
    if imc == 0:
        return "Altura inválida"
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso adequado"
    if imc < 30:
        return "Sobrepeso"
    return "Obesidade"

def calcular_agua_diaria_ml(peso: float) -> int:
    # regra prática: ~35 ml por kg de peso
    return int(round(peso * 35))

def calcular_exercicio_por_dia_min(imc: float) -> str:
    # recomendações gerais (OMS) adaptadas por faixa de IMC
    if imc == 0:
        return "—"
    if imc < 18.5:
        return "20–30 min/dia (leve) + força 2×/sem"
    if imc < 25:
        return "30–45 min/dia (moderado) + força 2–3×/sem"
    if imc < 30:
        return "45–60 min/dia (moderado) + força 3×/sem"
    return "60–90 min/dia (progressivo) + força 3×/sem"

def calcular_peso_ideal(altura: float, sexo: str) -> float:
    """
    Fórmula de Devine:
    - Masc: 50 + 2.3 * (altura em polegadas - 60)
    - Fem : 45.5 + 2.3 * (altura em polegadas - 60)
    """
    if altura <= 0:
        return 0.0
    polegadas = (altura * 100) / 2.54
    if sexo.upper().startswith("M"):  # Masculino
        return 50 + 2.3 * (polegadas - 60)
    else:  # Feminino (padrão)
        return 45.5 + 2.3 * (polegadas - 60)

import random

def frase_motivacional(nome: str, imc_class: str) -> str:
    base = f"{nome}, "
    
    frases_gerais = [
        "você é sua melhor versão em construção. 🌸",
        "o equilíbrio vem com o amor-próprio e a constância. 🌿",
        "pequenos cuidados diários constroem grandes mudanças. 💧",
        "seu corpo agradece cada escolha de bem-estar. ✨",
        "um passo de cada vez — mas nunca pare. 💪",
        "o autocuidado é a forma mais bonita de amor. 💖",
        "você merece se sentir leve, forte e feliz. ☀️",
        "cultive gentileza com você mesma todos os dias. 🌷",
        "respira, confia e continua — você está evoluindo. 🌙",
        "ser saudável é um ato de amor com quem você é. 🍃"
    ]

    frases_por_imc = {
        "Abaixo do peso": [
            "seu corpo é único. Fortaleça-se com carinho e paciência. 🌱",
            "cada refeição equilibrada é um gesto de amor por você. 💕",
        ],
        "Peso adequado": [
            "você está vibrando em equilíbrio. Continue se cuidando! 🌸",
            "mantenha o ritmo: corpo e mente em harmonia. 🌿",
        ],
        "Sobrepeso": [
            "tudo começa com um passo — e você já começou. 💪",
            "cada treino é um presente para o seu futuro. 🌞",
        ],
        "Obesidade": [
            "gentileza com o processo, consistência com o propósito. 🌷",
            "com amor e paciência, o impossível vira rotina. ✨",
        ]
    }

    # Seleciona frases conforme classificação do IMC
    frases_escolhidas = frases_por_imc.get(imc_class, frases_gerais)
    frase = random.choice(frases_escolhidas)
    return base + frase

    


# ===================== ENTRADAS =====================
with st.form("form_saude"):
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome")
        idade = st.number_input("Idade (anos)", min_value=0, max_value=120, step=1, value=25)
        sexo = st.selectbox("Sexo", ["Feminino", "Masculino"])
    with col2:
        altura = st.number_input("Altura (m)", min_value=1.0, max_value=2.5, step=0.01, value=1.65)
        peso = st.number_input("Peso (kg)", min_value=1.0, max_value=400.0, step=0.1, value=60.0)

    enviar = st.form_submit_button("Calcular ✅")

# ===================== RESULTADOS =====================
if enviar:
    imc = calcular_imc(peso, altura)
    classe = classificar_imc(imc)
    agua_ml = calcular_agua_diaria_ml(peso)
    exercicio = calcular_exercicio_por_dia_min(imc)
    peso_id = calcular_peso_ideal(altura, sexo)

    st.markdown("---")
    st.markdown("### 📊 Resultados")

    m1, m2, m3 = st.columns(3)
    m1.metric("IMC", f"{imc:.2f}", classe)
    m2.metric("Água por dia", f"{agua_ml} ml")
    m3.metric("Peso ideal", f"{peso_id:.1f} kg")

    st.markdown("### 🏃‍♀️ Recomendação de exercício")
    st.write(exercicio)

    st.markdown("### 💬 Mensagem motivacional")
    nome_display = nome.strip() if nome.strip() else "Você"
    st.success(frase_motivacional(nome_display, classe))
# --- Mensagem final motivacional ---
st.markdown("---")
st.subheader("💖 Mensagem de Motivação")
st.markdown("### 🎬 É se amando que tudo se transforma ✨")
st.video("https://app.heygen.com/videos/eb44f76d34604cd7b672b7b4d32e602c")
st.caption("O primeiro passo para cuidar do corpo é cuidar do coração. 💫")
    st.caption("⚠️ Dicas gerais. Para orientações específicas, procure um(a) profissional de saúde.")
# ==================== VÍDEO MOTIVACIONAL ====================
st.markdown("## 🌸 Mensagem em Vídeo")
st.video("https://raw.githubusercontent.com/rosalva1911-eng/programa-saude-fe/main/vídeo%20amor%20próprio.mp4")
