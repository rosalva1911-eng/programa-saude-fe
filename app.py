import streamlit as st
import os

# ==============================
# CONFIG (tem que ficar no topo)
# ==============================
st.set_page_config(
    page_title="Eu Já Existia Antes de Você",
    page_icon="💚",
    layout="centered"
)

# ==============================
# HELPERS
# ==============================
def show_image(path: str):
    """Mostra a imagem sem quebrar o app se o arquivo não existir."""
    if os.path.exists(path):
        st.image(path, use_container_width=True)
    else:
        st.warning(f"Imagem não encontrada: {path}")

# ==============================
# MENU
# ==============================
menu = st.sidebar.radio("Menu", ["📘 Livro", "💚 Saúde & Ferramentas"])

# ==============================
# PÁGINA LIVRO
# ==============================
def render_livro():
    st.title("📘 Eu Já Existia Antes de Você")
    st.markdown("*Um caminho de volta para si*")
    st.caption("Autora: Fhernânda Rocha")

    # CAPA (no seu repo está assim)
    show_image("00_capa.png.png")

    # ABERTURA
    st.markdown("---")
    st.subheader("Antes de tudo, um lembrete")
    st.markdown(
        "Antes de qualquer relacionamento, você já era alguém.\n\n"
        "Este livro começa no momento em que você se lembra de si."
    )
    show_image("01_lembrete.png.jpg")

    # CAPÍTULO 1
    st.markdown("---")
    st.subheader("Capítulo 1 — O Despertar")
    st.markdown(
        "O despertar começa quando você percebe que não era amor demais.\n\n"
        "Era a ausência de si. Aqui, a consciência começa a se formar."
    )
    show_image("02_lei_atracao_espelho.png.jpg")

    # CAPÍTULO 2
    st.markdown("---")
    st.subheader("Capítulo 2 — Quando você se abandona")
    st.markdown(
        "Nem sempre o fim dói apenas pela ausência do outro.\n\n"
        "Muitas vezes, dói porque, no caminho, você se deixou para trás."
    )
    show_image("03_quando_amor_termina.png.jpg")

    st.markdown(
        "Você tentou sustentar, compreender e não perder.\n\n"
        "E, aos poucos, foi se afastando de quem você era."
    )
    show_image("04_onde_se_perdeu.png.jpg")

    st.markdown(
        "Sentir não é falha. Amar não é erro.\n\n"
        "O que machuca é permanecer onde não há reciprocidade."
    )
    show_image("05_voce_nao_falhou.png.jpg")

    # CAPÍTULO 3
    st.markdown("---")
    st.subheader("Capítulo 3 — A energia não mente")
    st.markdown(
        "A energia não responde ao que você deseja.\n\n"
        "Ela responde ao que você sustenta emocionalmente."
    )
    show_image("06_lei_atracao_reflexiva.png.jpg")

    # CAPÍTULO 4
    st.markdown("---")
    st.subheader("Capítulo 4 — O retorno para si")
    st.markdown(
        "Retornar para si é um movimento de coragem.\n\n"
        "É parar de esperar que o outro mude e começar a se escolher."
    )
    show_image("07_nao_suplicar.png.jpg")

    st.markdown(
        "Parar de se abandonar é um compromisso diário.\n\n"
        "É respeitar limites, necessidades e o próprio ritmo."
    )
    # no seu print existe 14_voltar_para_si.png.jpg, então usei ele aqui
    show_image("14_voltar_para_si.png.jpg")

    st.markdown("Reconhecer o próprio valor é o ponto onde tudo se reorganiza.")
    show_image("09_reconheca_valor.png.jpg")

    # CAPÍTULO 5
    st.markdown("---")
    st.subheader("Capítulo 5 — Redes de sustentação")
    st.markdown(
        "Voltar para si não é caminhar sozinha.\n\n"
        "Relações saudáveis sustentam, acolhem e lembram quem você é."
    )
    show_image("10_amizades.png.jpg")

    # CAPÍTULO 6
    st.markdown("---")
    st.subheader("Capítulo 6 — Práticas de continuidade")
    st.markdown(
        "Consciência sem prática se perde.\n\n"
        "Aqui, você transforma entendimento em ação."
    )
    show_image("11_Checklist.png.jpg")

    st.markdown("Escrever é uma forma de escutar a si mesma.")
    show_image("12_como_escrever_carta.png.jpg")

    st.markdown("Agora, a palavra é sua.")
    show_image("13_carta_futuro.png.jpg")

    # CAPÍTULO 7
    st.markdown("---")
    st.subheader("Capítulo 7 — Saúde é autocuidado")
    st.markdown(
        "Cuidar da saúde não é punição.\n\n"
        "É presença no corpo e respeito aos limites."
    )
    show_image("15_saude_cuidar_corpo.png")
    show_image("16_saude_cuidado_verdade.png")
    show_image("17_saude_escute_corpo.png")
    show_image("18_saude_movivente-se.png")
    show_image("19_saude_movimento_escuta.png")
    show_image("20_saude_respeite_ritmo.png")

    # FINAL
    st.markdown("---")
    st.subheader("Permita-se florescer")
    st.markdown(
        "Você não chegou até aqui por acaso.\n\n"
        "Florescer não é virar outra pessoa.\n"
        "É lembrar quem você sempre foi."
    )
    show_image("21_permitase_florescer.png")

# ==============================
# PÁGINA SAÚDE (placeholder)
# ==============================
def render_saude():
    st.title("💚 Saúde & Ferramentas")
    st.info("Aqui a gente coloca o código da balança depois, quando você quiser. 😉")

# ==============================
# CHAMADA DO MENU
# ==============================
if menu == "📘 Livro":
    render_livro()
else:
    render_saude()
