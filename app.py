import streamlit as st

st.set_page_config(
    page_title="Eu Já Existia Antes de Você",
    page_icon="💚",
    layout="centered"
)

# ==============================
# 📘 LIVRO — CAPA + CAPÍTULO 1
# ==============================

st.title("📘 Eu Já Existia Antes de Você")
st.markdown("*Um caminho de volta para si*")
st.caption("Autora: Fhernânda Rocha")

# ✅ CAPA
st.image("00_capa.png.png", use_container_width=True)

# ✅ CAPÍTULO 1 — O DESPERTAR
st.markdown("---")
st.subheader("Capítulo 1 — O Despertar")
st.markdown(
    "O despertar começa quando você percebe que não era amor demais.\n\n"
    "Era a ausência de si. Aqui, a consciência começa a se formar."
)

st.image("02_lei_atracao_espelho.png.jpg", use_container_width=True)
