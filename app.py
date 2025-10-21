# ==============================
# 🌸 Programa Saúde da Fe 🌸
# ==============================
from typing import Any

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
st.markdown("Cuidar do corpo é um ato de amor-próprio. 💕")
st.subheader("Calculadora de IMC, Água, Exercício e Peso Ideal")
# ===================== VÍDEO MOTIVACIONAL =====================
st.markdown("### 💖 Mensagem de Motivação")
st.markdown("🎬 É se amando que tudo se transforma ✨")

# --- VÍDEO DO YOUTUBE (SEM AUTOPLAY) ---
video_id = "NsPiCrrfsT4"  # só o código do vídeo
st.markdown(
    f"""
    <div style="display:flex; justify-content:center; margin: 20px 0;">
        <iframe 
            width="560" 
            height="315" 
            src="https://www.youtube.com/embed/{video_id}?controls=1&rel=0&modestbranding=1" 
            title="Mensagem de Motivação"
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen
            style="border-radius: 16px; box-shadow: 0 0 12px rgba(0,0,0,0.2);"
        ></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

st.caption("💫 O primeiro passo para cuidar do corpo é cuidar do coração.")
st.markdown(
    "<p style='text-align:center; color:#e75480; font-size:1.1em;'>🌸 Cuidar de si é um ato de amor e consciência 🌸</p>",
    unsafe_allow_html=True)
st.write("Preencha seus dados e veja suas recomendações personalizadas. 🌿")


# ---------- FUNÇÕES ----------
def calcular_imc(peso: float, altura: float) -> float:
    if altura <= 0: return 0
    return peso / (altura ** 2)


def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso adequado"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"


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
    """

    :param altura:
    :param sexo:

    :return:
    :rtype: float
    """
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
        sexo: Any | None = st.selectbox("Sexo", ["F", "M"])
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


    def calcular_calorias_diarias(peso: float, altura: float, idade: int, sexo: str, objetivo: str) -> int:
        """
        Calcula a quantidade ideal de calorias por dia para atingir o peso desejado.
        Fórmula baseada na Taxa Metabólica Basal (TMB) e no objetivo do usuário.
        """


def calcular_calorias_diarias(tmb, objetivo, altura, sexo, nome=None):
    """
    Calcula as calorias diárias ajustadas conforme o objetivo,
    e retorna também o peso ideal e uma frase motivacional personalizada.
    """

    # Ajuste conforme o objetivo
    if objetivo.lower() == "emagrecer":
        calorias = tmb * 0.85  # déficit de 15%
    elif objetivo.lower() == "manter":
        calorias = tmb         # manutenção
    else:
        calorias = tmb * 1.15  # superávit para ganhar massa

    # Cálculo do peso ideal
    ideal = calcular_peso_ideal(altura, sexo)

    # Frase motivacional
    frase = frase_motivacional(nome.strip(), sexo) if nome else "Siga firme, o progresso é diário!"

    # Retorna todos os valores
    return int(calorias), ideal, frase
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
# ---------- BENEFÍCIOS DA KOMBUCHA ----------
st.markdown("---")
st.markdown("## 🍹 Benefícios da Kombucha")
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/5/5b/Kombucha_SCOBY.jpg",
    caption="Kombucha artesanal da Fê 🌸",
    use_container_width=True
)

st.markdown("""
A *Kombucha* é uma bebida probiótica natural, rica em enzimas, antioxidantes e micro-organismos benéficos ao intestino.  
Seu consumo regular pode ajudar a:

✅ Fortalecer o sistema imunológico  
✅ Melhorar a digestão e equilibrar a flora intestinal  
✅ Aumentar a energia e a disposição  
✅ Desintoxicar o organismo naturalmente  
✅ Promover bem-estar e equilíbrio corpo-mente 🌿  

> 🍶 “Cuidar do corpo é um ato de amor-próprio — e a Kombucha é uma aliada deliciosa nessa jornada.”
""")


# --- Seção: Benefícios do Kefir ---
def beneficios_kefir():
    st.title("🌿 Benefícios do Kefir - Saúde da Fê 🍶")

    st.write("""
    O kefir é uma bebida fermentada rica em *probióticos*, que ajudam a equilibrar a flora intestinal e fortalecem o sistema imunológico.  
    É natural, leve e pode ser consumido todos os dias como parte de um estilo de vida saudável. 💚
    """)

    st.subheader("✨ Principais Benefícios:")
    st.markdown("""
    - Melhora da *digestão* e redução do inchaço abdominal.  
    - Reforço da *imunidade natural*.  
    - Auxilia na *absorção de vitaminas e minerais*.  
    - Fonte de *cálcio, proteínas e vitaminas do complexo B*.  
    - Pode ajudar no *equilíbrio hormonal e intestinal*.  
    - Efeito *detox suave*, ajudando a eliminar toxinas.  
    """)

    st.info("💡 Dica da Fê: Consuma cerca de 100 a 200 ml por dia, de preferência em jejum ou com frutas.")

    st.success(
        "✨ Cuide da sua saúde naturalmente com amor, leveza e kombucha — o equilíbrio começa de dentro pra fora 🌸")


# ---------- RODAPÉ ----------
st.markdown("---")






