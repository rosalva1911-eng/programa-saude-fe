# =================================
# 🌸 Eu Ja Existia Antes De Você🌸
# =================================

# ---- MENU PRINCIPAL (NÃO APAGA NADA) ----
menu = st.sidebar.radio(
    "Menu",
    ["📘 Livro", "💚 Saúde & Ferramentas"],
)

def render_ferramentas():
    # ✅ AQUI DENTRO você vai colar TODO o código atual do seu app
    # (vídeo, balança, cálculos, tudo)
    pass

def render_livro():
    st.title("📘 Eu Já Existia Antes de Você")
    st.markdown("Um caminho de volta para si")
    st.caption("Autora: Fhernânda Rocha")

    # CAPA
    st.image("assets/00_capa.png", use_container_width=True)

    # ABERTURA
    st.markdown("---")
    st.subheader("Antes de tudo, um lembrete")
    st.markdown(
        "Antes de qualquer relacionamento, você já era alguém. "
        "Este livro começa no momento em que você se lembra de si."
    )
    st.image("assets/01_lembrete.png", use_container_width=True)
    # CAPÍTULO 1 — O DESPERTAR
st.markdown("---")
st.subheader("Capítulo 1 — O Despertar")
st.markdown(
    "O despertar começa quando você percebe que não era amor demais. "
    "Era a ausência de si. Aqui, a consciência começa a se formar."
)
st.image("assets/02_lei_atracao_espelho.png", use_container_width=True)

# ---------- CONFIGURAÇÃO (precisa ser uma das primeiras linhas) ----------
st.set_page_config(page_title="Eu Já Existia Antes deVocê", page_icon="💚", layout="centered")

# ---------- ESTILO ----------
st.markdown("""
<style>
.small-muted { color:#777; font-size:0.9rem; }
.card { padding:1rem; border-radius:12px; background:#fafafa; border:1px solid #eee; }
.stVideo {border-radius: 16px; box-shadow: 0px 0px 12px rgba(0,0,0,0.1);}
</style>
""", unsafe_allow_html=True)

# ---------- TÍTULO ----------
st.title("📘 Eu Já Existia Antes de Você")
st.markdown("*Um caminho de volta para si*")
st.caption("Autora: Fhernânda Rocha")


# ===================== VÍDEO MOTIVACIONAL =====================
st.markdown("### 💖 Mensagem de Motivação")
st.markdown("🎬 É se amando que tudo se transforma ✨")
video_id = "NsPiCrrfsT4"  # código do YouTube
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
st.write("Preencha seus dados e veja suas recomendações personalizadas. 🌿")

# ---------- FUNÇÕES ----------
def calcular_imc(peso: float, altura_m: float) -> float:
    if altura_m <= 0: 
        return 0.0
    return peso / (altura_m ** 2)

def classificar_imc(imc: float) -> str:
    if imc < 18.5:  return "Abaixo do peso"
    if imc < 25:    return "Peso adequado"
    if imc < 30:    return "Sobrepeso"
    if imc < 35:    return "Obesidade grau I"
    if imc < 40:    return "Obesidade grau II"
    return "Obesidade grau III"

def calcular_agua_diaria(peso: float) -> int:
    # regra prática: 35 ml por kg
    return int(round(peso * 35))

def calcular_tmb(sexo_F_ou_M: str, idade: int, peso: float, altura_cm: float) -> int:
    """Mifflin-St Jeor"""
    s = (sexo_F_ou_M or "F").upper()
    if s == "M":
        tmb = 10 * peso + 6.25 * altura_cm - 5 * idade + 5
    else:
        tmb = 10 * peso + 6.25 * altura_cm - 5 * idade - 161
    return int(round(tmb))

def calcular_exercicio(imc: float) -> str:
    if imc < 25:   return "30 min/dia (5x/sem) — foco em constância."
    if imc < 30:   return "45 min/dia (5–6x/sem) — cardio + força."
    return "60 min/dia (6x/sem) — começar leve e progredir."

def calcular_peso_ideal(altura_m: float, sexo_F_ou_M: str) -> float:
    """Devine: base 45.5(F)/50(M) + 0.9kg por cm acima de 152.4"""
    altura_cm = altura_m * 100
    s = (sexo_F_ou_M or "F").upper()
    base = 50.0 if s == "M" else 45.5
    extra_cm = max(0.0, altura_cm - 152.4)
    return round(base + 0.9 * extra_cm, 1)

def frase_motivacional(nome: str | None, classe_imc: str) -> str:
    frases = [
        "É se amando que tudo se transforma. 💫",
        "Seu corpo é sua casa: trate-o com carinho. 🌿",
        "Pequenos passos diários geram grandes mudanças. ✨",
        "Você merece cuidado, presença e gentileza. 💖",
        "Beber água é um abraço por dentro. 💧"
    ]
    base = random.choice(frases)
    pessoa = (nome or "Você").strip().split()[0].capitalize()
    return f"{pessoa}, {base}"

def calcular_calorias_diarias(tmb: int, objetivo: str, altura_m: float, sexo_F_ou_M: str, nome: str | None = None):
    """
    Ajusta calorias conforme objetivo e retorna (calorias, peso_ideal, frase).
    """
    obj = (objetivo or "").strip().lower()
    if obj == "emagrecer":
        calorias = tmb * 0.85       # ~15% déficit
    elif obj == "manter":
        calorias = tmb              # manutenção
    else:
        calorias = tmb * 1.15       # ~15% superávit

    ideal = calcular_peso_ideal(altura_m, sexo_F_ou_M)
    frase = frase_motivacional(nome, classificar_imc(calcular_imc(peso=70, altura_m=1.7)))  # dummy classe p/ tom positivo
    return int(round(calorias)), ideal, frase

def beneficios_kefir():
    st.subheader("🌿 Benefícios do Kefir")
    st.markdown("""
- Melhora da *digestão* e redução do inchaço abdominal.  
- Reforço da *imunidade*.  
- Auxilia na *absorção de vitaminas e minerais*.  
- Fonte de *cálcio, proteínas e vitaminas do complexo B*.  
- Pode ajudar no *equilíbrio intestinal*.  
- Efeito *detox suave*.  
""")
    st.info("💡 Dica da Fê: 100–200 ml/dia, em jejum ou com frutas.")

# ---------- FORMULÁRIO ----------
with st.form("form_saude"):
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome")
        idade = st.number_input("Idade", min_value=10, max_value=100, value=30, step=1)
        sexo_label = st.selectbox("Sexo", ["Feminino", "Masculino"])
        sexo = "F" if sexo_label == "Feminino" else "M"
    with col2:
        altura = st.number_input("Altura (m)", min_value=1.30, max_value=2.30, value=1.65, step=0.01, format="%.2f")
        peso = st.number_input("Peso (kg)", min_value=30.0, max_value=300.0, value=65.0, step=0.1, format="%.1f")

    objetivo = st.selectbox("Objetivo", ["Emagrecer", "Manter", "Ganhar massa"])
    enviar = st.form_submit_button("Calcular ✅")

# ---------- RESULTADOS ----------
if enviar:
    imc = calcular_imc(peso, altura)
    classe = classificar_imc(imc)
    agua = calcular_agua_diaria(peso)
    tmb = calcular_tmb(sexo, idade, peso, altura * 100)

    # >>> calcula calorias, peso ideal e frase ANTES de mostrar os cards
    calorias, ideal, frase = calcular_calorias_diarias(tmb, objetivo, altura, sexo, nome)

    st.markdown("---")
    st.markdown("### 📊 Resultados")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("IMC", f"{imc:.2f}", classe)
    with c2:
        st.metric("Água/dia", f"{agua} ml")
    with c3:
        st.metric("Peso ideal", f"{ideal:.1f} kg")
    with c4:
        st.metric("Calorias/dia", f"{calorias} kcal")

    st.markdown("### 🏃 Recomendação de exercício")
    st.write(calcular_exercicio(imc))

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
Consumo regular pode ajudar a:

✅ Fortalecer o sistema imunológico  
✅ Melhorar a digestão e equilibrar a flora intestinal  
✅ Aumentar a energia e a disposição  
✅ Desintoxicar naturalmente  
✅ Promover bem-estar corpo-mente 🌿  

> 🍶 “Cuidar do corpo é um ato de amor-próprio — e a Kombucha é uma aliada deliciosa nessa jornada.”
""")

# ---------- BENEFÍCIOS DO KEFIR (opcional em expander) ----------
with st.expander("🍶 Ver benefícios do Kefir"):
    beneficios_kefir()

# ---------- RODAPÉ ----------
st.markdown("---")
st.caption("Dica Fê: priorize sono, hidratação e fibras. Kombucha geladinha ajuda a rotina ficar gostosa! 🫶")
if menu == "📘 Livro":
    render_livro()
elif menu == "💚 Saúde & Ferramentas":
    render_ferramentas()
# ==============================
# 📘 LIVRO — EM CONSTRUÇÃO
# ==============================

def render_livro():
    st.title("📘 Eu Já Existia Antes de Você")
    st.markdown("*Um caminho de volta para si*")
    st.caption("Autora: Fhernânda Rocha")

    st.image("assets/00_capa.png", use_container_width=True)
