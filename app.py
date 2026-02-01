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
# ==============================
# 🔐 TELA DE ACESSO — CONTEÚDO EXCLUSIVO
# ==============================

if "acesso_liberado" not in st.session_state:
    st.session_state.acesso_liberado = False

if not st.session_state.acesso_liberado:
    st.title("🔐 Acesso exclusivo")
    st.markdown(
        "Este conteúdo é de uso pessoal e protegido.\n\n"
        "Digite seu **código de acesso** para continuar."
    )

    codigo = st.text_input(
        "Código de acesso",
        type="password",
        placeholder="Digite seu código aqui"
    )

    if st.button("Entrar"):
        if codigo == "Acesso2026":
            st.session_state.acesso_liberado = True
            st.rerun()
        else:
            st.error("Código inválido. Verifique e tente novamente.")

    st.stop()
# ==============================
# 🛑 BLOQUEIO DE CLIQUE DIREITO
# ==============================
st.markdown("""
<script>
document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
});
</script>
""", unsafe_allow_html=True)  

# ==============================
# 🔒 BLOQUEIO DE CÓPIA DE TEXTO
# ==============================
st.markdown("""
<style>
body {
    -webkit-user-select: none; /* Safari */
    -moz-user-select: none;    /* Firefox */
    -ms-user-select: none;     /* IE/Edge */
    user-select: none;         /* Padrão */
}
</style>
""", unsafe_allow_html=True)
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
# 🎬 VÍDEO DE BOAS-VINDAS
st.markdown("### 🌿 Bem-vinda a este espaço")

video_motivacional("B_Uy5AI9L7E")

st.markdown(
    "_Este não é um livro para ser lido com pressa. "
    "Permita-se sentir, pausar e seguir no seu ritmo._"
)

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

# 🎬 Vídeo — Reflexão sobre a Lei da Atração
st.markdown("### ✨ Uma pausa para refletir sobre seus pensamentos")

video_motivacional("a-v0uwv6rh0")

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
# ==============================
# CAPÍTULO — 45 LEIS DE UMA MULHER DE ALTO VALOR
# ==============================
st.markdown("---")
st.subheader("🌹 45 Leis de uma Mulher de Alto Valor no Relacionamento")
st.markdown(
    "_Não para controlar o outro — mas para não se abandonar._"
)
# 🎬 Vídeo — As 45 Leis de uma Mulher de Alto Valor
st.markdown("### 🌹 Uma mensagem para fortalecer seu posicionamento")

video_motivacional("eHN7ertzvi0")

st.markdown(
    "_Essas leis não existem para punir. Elas existem para proteger sua paz e sustentar relações conscientes._"
)

st.markdown("""
Essas leis não nasceram da dureza.  
Nasceram da consciência.

Ser uma mulher de alto valor não é sobre superioridade.  
É sobre **coerência interna**.

Elas existem para proteger a minha paz,  
honrar meu valor  
e sustentar relações mais conscientes.
""")

# 🧠 Leis emocionais
st.markdown("### 🧠 Leis emocionais")
st.markdown("""
- Eu não imploro atenção.  
- Eu não persigo quem não me escolhe.  
- Eu observo atitudes, não promessas.  
- Eu não justifico desrespeito.  
- Eu confio mais no que sinto do que no que escuto.  
- Eu não negocio minha paz.  
- Eu não tenho medo de ficar sozinha.  
- Eu não entro em disputas emocionais.  
- Eu não tento provar meu valor.  
- Eu escolho reciprocidade.
""")

# 💬 Leis de comunicação
st.markdown("### 💬 Leis de comunicação")
st.markdown("""
- Eu falo com clareza e respeito.  
- Eu não explico excessivamente meus limites.  
- Eu não discuto quando estou desvalorizada.  
- Eu não uso silêncio como punição, mas como proteção.  
- Eu não respondo impulsivamente.  
- Eu não levanto a voz para ser ouvida.  
- Eu não aceito migalhas emocionais.  
- Eu não insisto onde não há diálogo.  
- Eu não reajo, eu escolho.  
- Eu me retiro quando necessário.
""")

# 👑 Leis de autoestima
st.markdown("### 👑 Leis de autoestima")
st.markdown("""
- Eu me trato como prioridade.  
- Eu cuido do meu corpo, mente e energia.  
- Eu não me diminuo para caber.  
- Eu não comparo meu valor com o de ninguém.  
- Eu honro quem eu sou.  
- Eu não dependo emocionalmente.  
- Eu não abandono meus sonhos por alguém.  
- Eu me valorizo antes de ser valorizada.  
- Eu confio na minha intuição.  
- Eu não me sinto culpada por me escolher.
""")

# ❤️ Leis no amor
st.markdown("### ❤️ Leis no amor")
st.markdown("""
- Amor saudável não dói constantemente.  
- Quem quer, demonstra.  
- Interesse não confunde.  
- Presença vale mais que palavras bonitas.  
- Amor precisa de segurança emocional.  
- Eu não tento consertar alguém.  
- Eu não salvo quem não quer mudar.  
- Eu não romantizo falta de esforço.  
- Eu escolho relações conscientes.  
- Eu permito apenas quem soma.
""")

# 🌱 Leis de maturidade feminina
st.markdown("### 🌱 Leis de maturidade feminina")
st.markdown("""
- Eu aceito quando não é para mim.  
- Eu encerro ciclos sem drama.  
- Eu aprendo com cada experiência.  
- Eu cresço, não endureço.  
- Eu sei o meu valor — e ajo de acordo com ele.
""")

st.markdown("""
> Essas leis não me afastam do amor.  
> Elas me aproximam de mim.
""")

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
# 🎬 Vídeo de transição — autocuidado
st.markdown("### 🌿 Uma pausa para refletir")

video_motivacional("ZylGCem4zb0")

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
# 🧘‍♀️ MEDITAÇÃO — VOLTAR PARA SI
st.markdown("### 🧘‍♀️ Uma pausa para voltar para si")

st.markdown(
    "_Encontre uma posição confortável. "
    "Se puder, feche os olhos. "
    "Este é um momento só seu._"
)

video_motivacional("MXDVFHvLEIs")

st.markdown(
    "_Permaneça aqui o tempo que precisar. "
    "Você pode voltar para si quantas vezes quiser._"
)
# 🎬 VÍDEO DE ENCERRAMENTO — PERMITA-SE FLORESCER
st.markdown("### 🌸 Permita-se florescer")

video_motivacional("r63QJvI4Hvw")

st.markdown(
    "_Leve com você tudo o que sentiu aqui. "
    "Siga no seu tempo, com gentileza e verdade._"
)

imagem_com_zoom("21_permitase_florescer.png")


