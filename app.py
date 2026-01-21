import streamlit as st
import random

st.set_page_config(
    page_title="Eu Já Existia Antes de Você",
    page_icon="💚",
    layout="centered"
)

menu = st.sidebar.radio(
    "Menu",
    ["📘 Livro", "💚 Saúde & Ferramentas"]
) 
def render_livro():
    st.title("📘 Eu Já Existia Antes de Você")
    st.markdown("**Um caminho de volta para si**")
    st.caption("Autora: Fhernânda Rocha")

    # CAPA
    st.image("assets/00_capa.png", use_container_width=True)

    # CAPÍTULO 1 — O DESPERTAR
    st.markdown("---")
    st.subheader("Capítulo 1 — O Despertar")
    st.markdown(
        "O despertar começa quando você percebe que não era amor demais. "
        "Era a ausência de si. Aqui, a consciência começa a se formar."
    )
    st.image("assets/02_lei_atracao_espelho.png", use_container_width=True)
    # -------------------------------
    # CAPÍTULO 2 — QUANDO VOCÊ SE ABANDONA
    st.markdown("---")
    st.subheader("Capítulo 2 — Quando você se abandona")
    st.markdown(
        "Nem sempre o fim dói apenas pela ausência do outro. "
        "Muitas vezes, dói porque, no caminho, você se deixou para trás."
    )

    st.image("assets/03_quando_amor_termina.png", use_container_width=True)

    st.markdown(
        "Você tentou compreender, sustentar e não perder. "
        "E, aos poucos, foi se afastando de quem você era."
    )
    st.image("assets/04_onde_se_perdeu.png", use_container_width=True)

    st.markdown(
        "Sentir não é falha. Amar não é erro. "
        "O que machuca é permanecer onde não há reciprocidade."
    )
    st.image("assets/05_voce_nao_falhou.png", use_container_width=True)

    # -------------------------------
    # CAPÍTULO 3 — A ENERGIA NÃO MENTE
    st.markdown("---")
    st.subheader("Capítulo 3 — A energia não mente")
    st.markdown(
        "A energia não responde ao que você deseja, "
        "ela responde ao que você sustenta emocionalmente. "
        "Aqui, você começa a assumir a própria responsabilidade sem culpa."
    )
    st.image("assets/06_lei_atracao_reflexiva.png", use_container_width=True)

    # -------------------------------
    # CAPÍTULO 4 — O RETORNO PARA SI
    st.markdown("---")
    st.subheader("Capítulo 4 — O retorno para si")
    st.markdown(
        "Retornar para si é um movimento de coragem. "
        "É parar de esperar que o outro mude e começar a se escolher."
    )

    st.image("assets/07_nao_suplicar.png", use_container_width=True)

    st.markdown(
        "Parar de se abandonar é um compromisso diário. "
        "É respeitar limites, necessidades e o próprio ritmo."
    )
    st.image("assets/08_parar_abandonar.png", use_container_width=True)

    st.markdown(
        "Reconhecer o próprio valor é o ponto onde tudo se reorganiza. "
        "Você não precisa diminuir quem você é para caber em ninguém."
    )
    st.image("assets/09_reconheca_valor.png", use_container_width=True)

    # -------------------------------
    # CAPÍTULO 5 — REDES DE SUSTENTAÇÃO
    st.markdown("---")
    st.subheader("Capítulo 5 — Redes de sustentação")
    st.markdown(
        "Voltar para si não é caminhar sozinha. "
        "As relações saudáveis sustentam, acolhem e lembram quem você é "
        "quando o mundo parece pesado demais."
    )
    st.image("assets/10_amizades.png", use_container_width=True)

    # -------------------------------
    # CAPÍTULO 6 — PRÁTICAS DE CONTINUIDADE
    st.markdown("---")
    st.subheader("Capítulo 6 — Práticas de continuidade")
    st.markdown(
        "Consciência sem prática se perde. "
        "Aqui, você transforma o que entendeu em ações simples, possíveis e sustentáveis."
    )

    st.markdown(
        "Pequenas escolhas diárias constroem grandes mudanças. "
        "Este checklist é um convite para se escolher todos os dias."
    )
    st.image("assets/11_checklist.png", use_container_width=True)

    st.markdown(
        "Escrever é uma forma de escutar a si mesma. "
        "Esta carta é um gesto de cuidado com quem você está se tornando."
    )
    st.image("assets/12_como_escrever_carta.png", use_container_width=True)

    st.markdown(
        "Agora, a palavra é sua. "
        "Escreva sem pressa, sem censura e com verdade."
    )
    st.image("assets/13_carta_futuro.png", use_container_width=True)

    # -------------------------------
    # CAPÍTULO 7 — SAÚDE É AUTOCUIDADO
    st.markdown("---")
    st.subheader("Capítulo 7 — Saúde é autocuidado")
    st.markdown(
        "Cuidar da saúde não é cobrança nem punição. "
        "É presença no corpo, escuta dos sinais e respeito aos próprios limites."
    )

    st.markdown(
        "O corpo é a casa onde a sua energia habita. "
        "Cuidar dele é um gesto de respeito e amor-próprio."
    )
    st.image("assets/15_saude_cuidar_corpo.png", use_container_width=True)

    st.markdown(
        "Cuidado de verdade não machuca, não exige perfeição "
        "e não nasce da culpa. Ele nasce do acolhimento."
    )
    st.image("assets/16_saude_cuidado_verdade.png", use_container_width=True)

    st.markdown(
        "O corpo fala o tempo todo. "
        "Aprender a escutá-lo muda a forma como você vive."
    )
    st.image("assets/17_saude_escute_corpo.png", use_container_width=True)

    st.markdown(
        "Movimento é diálogo com o corpo, não castigo. "
        "Escolha se mover por você, não contra você."
    )
    st.image("assets/18_saude_movimente_se.png", use_container_width=True)

    st.markdown(
        "Quando você se move com presença, "
        "o corpo responde com mais vitalidade e equilíbrio."
    )
    st.image("assets/19_saude_movimento_escuta.png", use_container_width=True)

    st.markdown(
        "Respeitar o próprio ritmo é um dos maiores atos de autocuidado. "
        "Seu corpo sabe o tempo certo das coisas."
    )
    st.image("assets/20_saude_respeite_ritmo.png", use_container_width=True)

    # -------------------------------
    # CAPÍTULO FINAL — PERMITA-SE FLORESCER
    st.markdown("---")
    st.subheader("Permita-se florescer")
    st.markdown(
        "Você não chegou até aqui por acaso. "
        "Cada página lida foi um passo de volta para si.\n\n"
        "Florescer não é virar outra pessoa. "
        "É lembrar quem você sempre foi antes de se esquecer.\n\n"
        "Permita-se crescer no seu tempo, "
        "honrar suas emoções, respeitar seus ciclos "
        "e escolher caminhos que sustentem quem você é.\n\n"
        "Que você siga se escolhendo, "
        "com gentileza, coragem e verdade.\n\n"
        "Você já existia antes de qualquer dor. "
        "E continuará existindo — agora, mais inteira."
    )
    st.image("assets/21_permitase_florescer.png", use_container_width=True)

     # =================================
     # 🌸 Eu Já Existia Antes De Você 🌸
     # =================================

 import random
 import streamlit as st
 
 # ---------- CONFIGURAÇÃO (precisa ser uma das primeiras linhas) ----------
 st.set_page_config(page_title="Eu Já Existia Antes de Você", page_icon="💚", layout="centered")
 
 # ---------- ESTILO ----------
 st.markdown("""
 <style>
 .small-muted { color:#777; font-size:0.9rem; }
 .card { padding:1rem; border-radius:12px; background:#fafafa; border:1px solid #eee; }
 .stVideo {border-radius: 16px; box-shadow: 0px 0px 12px rgba(0,0,0,0.1);}
 </style>
 """, unsafe_allow_html=True)
 
 
 # ---- MENU PRINCIPAL (NÃO APAGA NADA) ----
 menu = st.sidebar.radio(
     "Menu",
     ["📘 Livro", "💚 Saúde & Ferramentas"],
 )
 
 
 # ============================================================
 # 💚 SAÚDE & FERRAMENTAS  (AQUI VAI O SEU CÓDIGO ATUAL INTEIRO)
 # ============================================================
 def render_ferramentas():
 
     # ===================== VÍDEO MOTIVACIONAL =====================
     st.title("📘 Eu Já Existia Antes de Você")
     st.markdown("*Um caminho de volta para si*")
     st.caption("Autora: Fhernânda Rocha")
 
     st.markdown(" 💖 Mensagem de Motivação")
     st.markdown("🎬 É se amando que tudo se transforma ✨")
     video_id = "NsPiCrrfsT4"  # código do YouTube
     st.markdown(
         """
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
         """
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
         frase = frase_motivacional(nome, classificar_imc(calcular_imc(peso=70, altura_m=1.7)))
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
 
     # ---------- BENEFÍCIOS DO KEFIR ----------
     with st.expander("🍶 Ver benefícios do Kefir"):
         beneficios_kefir()
 
     # ---------- RODAPÉ ----------
     st.markdown("---")
     st.caption("Dica Fê: priorize sono, hidratação e fibras. Kombucha geladinha ajuda a rotina ficar gostosa! 🫶")
 

 # ============================================================
 # CHAMADA DO MENU
 # ============================================================
 if menu == "📘 Livro":
     render_livro()
 elif menu == "💚 Saúde & Ferramentas":
     render_ferramentas()
