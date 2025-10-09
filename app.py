import streamlit as st

# ===================== CONFIG =====================
st.set_page_config(page_title="Programa Saúde da Fê 💧", page_icon="🌿", layout="centered")
st.title("🌸 Programa Saúde da Fê")
st.subheader("Calculadora de IMC, Água, Exercício e Peso Ideal")

st.write("Preencha seus dados e veja suas recomendações personalizadas. 💪🍃")

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

def frase_motivacional(nome: str, imc_class: str) -> str:
    base = f"{nome}, "
    frases = {
        "Abaixo do peso": base + "seu corpo é único. Vamos fortalecer com calma: constância vence pressa. 🌱",
        "Peso adequado": base + "você está no caminho certo! Mantenha o equilíbrio: movimento, água e descanso. ✨",
        "Sobrepeso": base + "cada passo conta. Foque no progresso diário — pequenas vitórias geram grandes resultados. 💪",
        "Obesidade": base + "respeite o seu tempo. Com consistência e cuidado, você vai mais longe do que imagina. 🌟",
        "Altura inválida": "Preencha seus dados corretamente para eu te ajudar direitinho. 🙂",
    }
    return frases.get(imc_class, base + "você consegue! Um dia de cada vez, com carinho por você. 💖")

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

    st.caption("⚠️ Dicas gerais. Para orientações específicas, procure um(a) profissional de saúde.")
