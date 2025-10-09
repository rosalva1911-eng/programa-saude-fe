import streamlit as st

# --- título e introdução ---
st.set_page_config(page_title="Programa Saúde da Fê 💧", page_icon="🌿", layout="centered")

st.title("🌸 Programa Saúde da Fê")
st.subheader("Calculadora de Peso Ideal")

st.write("Descubra seu **peso ideal** com base na altura e no sexo. 🧘‍♀️")

# --- entrada de dados ---
altura = st.number_input("Digite sua altura (em metros):", min_value=1.0, max_value=2.5, step=0.01)
sexo = st.selectbox("Selecione seu sexo:", ["Feminino", "Masculino"])

# --- função de cálculo ---
def calcular_peso_ideal(altura, sexo):
    if sexo == "Masculino":
        return 50 + 2.3 * ((altura * 100 / 2.54) - 60)
    else:
        return 45.5 + 2.3 * ((altura * 100 / 2.54) - 60)

# --- botão para calcular ---
if st.button("Calcular Peso Ideal 💪"):
    if altura > 0:
        peso_ideal = calcular_peso_ideal(altura, sexo)
        st.success(f"Seu peso ideal é **{peso_ideal:.1f} kg** 🩷")
        st.balloons()
    else:
        st.warning("Por favor, insira uma altura válida.")
