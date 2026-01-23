import streamlit as st

# ==============================
# CONFIGURAÇÃO
# ==============================
st.set_page_config(
    page_title="Eu Já Existia Antes de Você",
    page_icon="💚",
    layout="centered"
)

# ==============================
# FUNÇÃO: IMAGEM COM ZOOM
# ==============================
def imagem_com_zoom(caminho: str, legenda: str = "🔍 Ampliar imagem para leitura"):
    st.image(caminho, use_container_width=True)
    with st.expander(legenda):
        st.image(caminho, use_container_width=True)

# ==============================
# TÍTULO DO LIVRO
# ==============================
st.title("📘 Eu Já Existia Antes de Você")
st.markdown("*Um caminho de volta para si*")
st.caption("Autora: Fhernânda Rocha")

# ==============================
# CAPA
# ==============================
imagem_com_zoom("00_capa.png.png")

# ==============================
# ABERTURA
# ==============================
st.markdown("---")
st.subheader("Antes de tudo, um lembrete")
st.markdown(
    "Antes de qualquer relacionamento, você já era alguém.\n\n"
    "Este livro começa no momento em que você se lembra de si."
)
imagem_com_zoom("01_lembrete.png.jpg")

# ==============================
# CAPÍTULO 1 — O DESPERTAR
# ==============================
st.markdown("---")
st.subheader("Capítulo 1 — O Despertar")
st.markdown(
    "O despertar começa quando você percebe que não era amor demais.\n\n"
    "Era a ausência de si. Aqui, a consciência começa a se formar."
)
imagem_com_zoom("02_lei_atracao_espelho.png.jpg")

# ==============================
# CAPÍTULO 2 — QUANDO VOCÊ SE ABANDONA
# ==============================
st.markdown("---")
st.subheader("Capítulo 2 — Quando você se abandona")
st.markdown(
    "Nem sempre o fim dói apenas pela ausência do outro.\n\n"
    "Muitas vezes, dói porque, no caminho, você se deixou para trás."
)
imagem_com_zoom("03_quando_amor_termina.png.jpg")

st.markdown(
    "Você tentou sustentar, compreender e não perder.\n\n"
    "E, aos poucos, foi se afastando de quem você era."
)
imagem_com_zoom("04_onde_se_perdeu.png.jpg")

st.markdown(
    "Sentir não é falha. Amar não é erro.\n\n"
    "O que machuca é permanecer onde não há reciprocidade."
)
imagem_com_zoom("05_voce_nao_falhou.png.jpg")

# ==============================
# CAPÍTULO 3 — A ENERGIA NÃO MENTE
# ==============================
st.markdown("---")
st.subheader("Capítulo 3 — A energia não mente")
st.markdown(
    "A energia não responde ao que você deseja.\n\n"
    "Ela responde ao que você sustenta emocionalmente."
)
imagem_com_zoom("06_lei_atracao_reflexiva.png.jpg")

# ==============================
# CAPÍTULO 4 — O RETORNO PARA SI
# ==============================
st.markdown("---")
st.subheader("Capítulo 4 — O retorno para si")
st.markdown(
    "Retornar para si é um movimento de coragem.\n\n"
    "É parar de esperar que o outro mude e começar a se escolher."
)
imagem_com_zoom("07_nao_suplicar.png.jpg")

st.markdown(
    "Parar de se abandonar é um compromisso diário.\n\n"
    "É respeitar limites, necessidades e o próprio ritmo."
)
imagem_com_zoom("14_voltar_para_si.png.jpg")

st.markdown("Reconhecer o próprio valor é o ponto onde tudo se reorganiza.")
imagem_com_zoom("09_reconheca_valor.png.jpg")

# ==============================
# CAPÍTULO 5 — REDES DE SUSTENTAÇÃO
# ==============================
st.markdown("---")
st.subheader("Capítulo 5 — Redes de sustentação")
st.markdown(
    "Voltar para si não é caminhar sozinha.\n\n"
    "Relações saudáveis sustentam, acolhem e lembram quem você é "
    "quando o mundo parece pesado demais."
)
imagem_com_zoom("10_amizades.png.jpg")

# ==============================
# CAPÍTULO 6 — PRÁTICAS DE CONTINUIDADE
# ==============================
st.markdown("---")
st.subheader("Capítulo 6 — Práticas de continuidade")
st.markdown(
    "Consciência sem prática se perde.\n\n"
    "Aqui, você transforma o que entendeu em ações simples, possíveis e sustentáveis."
)

st.markdown(
    "Pequenas escolhas diárias constroem grandes mudanças.\n\n"
    "Este checklist é um convite para se escolher todos os dias."
)
imagem_com_zoom("11_Checklist.png.jpg")

st.markdown(
    "Escrever é uma forma de escutar a si mesma.\n\n"
    "Esta carta é um gesto de cuidado com quem você está se tornando."
)
imagem_com_zoom("12_como_escrever_carta.png.jpg")

st.markdown(
    "Agora, a palavra é sua.\n\n"
    "Escreva sem pressa, sem censura e com verdade."
)
imagem_com_zoom("13_carta_futuro.png.jpg")
