import streamlit as st
import random
# ==============================
# CONFIGURAÇÃO
# ==============================
st.set_page_config(
    page_title="Eu Já Existia Antes de Você",
    page_icon="💚",
    layout="centered"
)
# =====================
# FUNÇÃO: EFEITOS FLUTUANDO
# =====================
def efeitos_flutuando(tema: str = "flores"):
    if tema == "corações":
        itens = ["❤️", "💗", "💖", "💕", "💘"]
    else:
        itens = ["🌸", "🌷", "🌺", "💐", "✨"]

    elementos_html = ""
    for _ in range(18):
        left = random.randint(0, 100)
        delay = random.random() * 4
        dur = random.uniform(6, 12)
        size = random.uniform(16, 32)
        char = random.choice(itens)

        elementos_html += f"""
        <span class="floaty" style="
            left:{left}%;
            animation-delay:{delay}s;
            animation-duration:{dur}s;
            font-size:{size}px;
        ">{char}</span>
        """

    st.markdown(
        f"""
        <style>
        .fx-layer {{
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 999999;
            overflow: hidden;
        }}
        .floaty {{
            position: absolute;
            bottom: -40px;
            opacity: 0.85;
            animation-name: rise;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
        }}
        @keyframes rise {{
            0% {{ transform: translateY(0); opacity: 0; }}
            10% {{ opacity: 0.9; }}
            100% {{ transform: translateY(-110vh); opacity: 0; }}
        }}
        </style>

        <div class="fx-layer">
            {elementos_html}
        </div>
        """,
        unsafe_allow_html=True
    )
# ==============================
# FUNÇÃO: IMAGEM COM ZOOM
# ==============================
def imagem_com_zoom(caminho: str, legenda="🔍 Abrir imagem para leitura"):
    st.image(caminho, use_container_width=True)

    # Botão para celular (abre fora / em tela cheia)
    st.link_button(
        legenda,
        caminho
    )

def video_motivacional(video_id="NsPiCrrfsT4"):
    st.markdown("### 💖 Mensagem de Motivação")
    st.markdown("🎬 É se amando que tudo se transforma ✨")
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
        unsafe_allow_html=True
    )
st.sidebar.markdown("✨ **Efeitos visuais**")

ativar_efeitos = st.sidebar.toggle(
    "Ativar corações/flores",
    value=True
)

tema_efeito = st.sidebar.selectbox(
    "Tema",
    ["flores", "corações"]
)

if ativar_efeitos:
    efeitos_flutuando(tema_efeito)
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
video_motivacional()

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

# 🎬 PAUSA DE CONSCIÊNCIA — EU JÁ EXISTIA ANTES DE VOCÊ
video_motivacional("PMLO-uV2s4s")

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

video_motivacional("LunWAyKmTPU")

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

# ==============================
# CAPÍTULO 7 — SAÚDE É AUTOCUIDADO
# ==============================
st.markdown("---")
st.subheader("Capítulo 7 — Saúde é autocuidado")
st.markdown(
    "Cuidar da saúde não é cobrança nem punição.\n\n"
    "É presença no corpo, escuta dos sinais e respeito aos próprios limites."
)

st.markdown(
    "O corpo é a casa onde a sua energia habita.\n\n"
    "Cuidar dele é um gesto de respeito e amor-próprio."
)
imagem_com_zoom("15_saude_cuidar_corpo.png")

st.markdown(
    "Cuidado de verdade não machuca, não exige perfeição "
    "e não nasce da culpa.\n\n"
    "Ele nasce do acolhimento."
)
imagem_com_zoom("16_saude_cuidado_verdade.png")

st.markdown(
    "O corpo fala o tempo todo.\n\n"
    "Aprender a escutá-lo muda a forma como você vive."
)
imagem_com_zoom("17_saude_escute_corpo.png")

st.markdown(
    "Movimento é diálogo com o corpo, não castigo.\n\n"
    "Escolha se mover por você, não contra você."
)
imagem_com_zoom("18_saude_movivente-se.png")

st.markdown(
    "Quando você se move com presença, "
    "o corpo responde com mais vitalidade e equilíbrio."
)
imagem_com_zoom("19_saude_movimento_escuta.png")

st.markdown(
    "Respeitar o próprio ritmo é um dos maiores atos de autocuidado.\n\n"
    "Seu corpo sabe o tempo certo das coisas."
)
imagem_com_zoom("20_saude_respeite_ritmo.png")

# ==============================
# ENCERRAMENTO — PERMITA-SE FLORESCER
# ==============================
st.markdown("---")
st.subheader("Permita-se florescer")
st.markdown(
    "Você não chegou até aqui por acaso.\n\n"
    "Cada página lida foi um passo de volta para si.\n\n"
    "Florescer não é virar outra pessoa.\n"
    "É lembrar quem você sempre foi antes de se esquecer.\n\n"
    "Permita-se crescer no seu tempo,\n"
    "honrar suas emoções,\n"
    "respeitar seus ciclos\n"
    "e escolher caminhos que sustentem quem você é.\n\n"
    "Você já existia antes de qualquer dor.\n"
    "E continuará existindo — agora, mais inteira."
)

imagem_com_zoom("21_permitase_florescer.png")


