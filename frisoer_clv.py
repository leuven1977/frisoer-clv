import streamlit as st

st.set_page_config(page_title="Kundeværdi-beregner for frisører", page_icon="💇‍♀️", layout="centered")

# --- Toptekst ---
st.title("💇‍♀️ Hvad er en ny kunde egentlig værd for din salon?")
st.markdown("""
Denne beregner er skabt for at vise frisører, **hvor vigtig en enkelt kunde egentlig er** – 
og hvorfor løbende nye kunder er nøglen til vækst.

Jeg hjælper **selvstændige frisører** med at skabe vækst og overskud i hverdagen – 
**med mere frihed, bedre løn og ro i maven.**

Med **16 års erfaring i marketing** og som **tidligere partner i en frisørsalon**, 
hjælper jeg dig med at få **styr på kunder, strategi og forretning.**
""")

st.divider()

# --- Damekunder ---
st.header("💇‍♀️ Damekunder")
with st.container():
    d_new = st.number_input("Antal nye kunder", min_value=0, value=1, step=1, key="d_new")
    d_price = st.number_input("Gennemsnitlig pris pr. klip", min_value=0, value=450, step=50, key="d_price")
    d_color = st.number_input("Pris på farve eller striber", min_value=0, value=700, step=50, key="d_color")
    d_color_freq = st.selectbox("Hvor ofte får kunden farve/striber?", 
                                ["Hver gang", "Hver 2. gang", "Hver 3. gang", "Hver 4. gang", "Aldrig"], 
                                index=1, key="d_color_freq")
    d_prod = st.number_input("Produktsalg pr. besøg", min_value=0, value=75, step=5, key="d_prod")
    d_visits = st.selectbox("Besøg pr. år", [4, 6, 8, 10, 12], index=2, key="d_visits")
    d_years = st.selectbox("Antal år som kunde", [1,2,3,4,5,6,7,8,9,10], index=3, key="d_years")

    if st.button("Beregn damekundeværdi", key="d_calc"):
        freq_map = {"Hver gang": 1.0, "Hver 2. gang": 0.5, "Hver 3. gang": 1/3, "Hver 4. gang": 0.25, "Aldrig": 0.0}
        color_factor = freq_map[d_color_freq]
        d_total = d_new * ((d_price + (d_color * color_factor) + d_prod) * d_visits * d_years)
        st.success(f"💇‍♀️ Estimeret livstidsværdi for damekunder: {int(d_total):,} kr.".replace(",", "."))

st.divider()

# --- Herrekunder ---
st.header("💇‍♂️ Herrekunder")
with st.container():
    m_new = st.number_input("Antal nye kunder", min_value=0, value=1, step=1, key="m_new")
    m_price = st.number_input("Gennemsnitlig pris pr. besøg", min_value=0, value=300, step=25, key="m_price")
    m_prod = st.number_input("Produktsalg pr. besøg", min_value=0, value=50, step=5, key="m_prod")
    m_visits = st.selectbox("Besøg pr. år", [4, 6, 8, 10, 12], index=3, key="m_visits")
    m_years = st.selectbox("Antal år som kunde", [1,2,3,4,5,6,7,8,9,10], index=3, key="m_years")

    if st.button("Beregn herrekundeværdi", key="m_calc"):
        m_total = m_new * ((m_price + m_prod) * m_visits * m_years)
        st.success(f"💇‍♂️ Estimeret livstidsværdi for herrekunder: {int(m_total):,} kr.".replace(",", "."))

st.divider()

# --- Børnekunder ---
st.header("🧒 Børnekunder")
with st.container():
    b_new = st.number_input("Antal nye kunder", min_value=0, value=1, step=1, key="b_new")
    b_price = st.number_input("Gennemsnitlig pris pr. besøg", min_value=0, value=250, step=25, key="b_price")
    b_prod = st.number_input("Produktsalg pr. besøg", min_value=0, value=30, step=5, key="b_prod")
    b_visits = st.selectbox("Besøg pr. år", [1, 2, 3, 4, 6], index=1, key="b_visits")
    b_years = st.selectbox("Antal år som kunde", [1,2,3,4,5,6,7,8,9,10], index=3, key="b_years")

    if st.button("Beregn børnekundeværdi", key="b_calc"):
        b_total = b_new * ((b_price + b_prod) * b_visits * b_years)
        st.success(f"🧒 Estimeret livstidsværdi for børnekunder: {int(b_total):,} kr.".replace(",", "."))

st.divider()

# --- Samlet beregning ---
st.header("📊 Samlet beregning")
if st.button("Vis samlet potentiale", key="total_calc"):
    try:
        total = d_total + m_total + b_total
        st.success(f"💰 Samlet estimeret livstidsværdi: {int(total):,} kr.".replace(",", "."))
    except NameError:
        st.warning("Beregn først værdien for alle tre kundetyper for at se totalen.")

st.divider()

# --- CTA sektion ---
st.markdown("""
### 💬 Ønsker du flere loyale kunder – uden at miste overblikket?

Beregneren er skabt for at hjælpe frisører med at forstå, hvor meget en kunde egentlig er værd – 
og hvorfor løbende nye kunder er nøglen til vækst.

Jeg hjælper **frisører, der vil have styr på deres forretning, økonomi og frihed.**

👉 [Book et gratis møde på Klary.dk](https://www.klary.dk)  
🔗 [Besøg min LinkedIn-profil](https://www.linkedin.com/in/michael-christensen-dk/)  
📞 Ring direkte på **28 10 96 68**
""")

st.divider()
st.caption("© 2025 Klary.dk – Uvildig rådgivning for selvstændige frisører.")
