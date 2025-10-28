import streamlit as st

st.set_page_config(page_title="Frisør – Kundens livstidsværdi", page_icon="💇‍♀️", layout="centered")

# --- Custom CSS ---
st.markdown("""
<style>
body {
    background-color: #ffffff;
    color: #333333;
    font-family: 'Inter', sans-serif;
}
h1, h2, h3 {
    color: #5a2ca0;
}
.section {
    background-color: #f8f8f8;
    padding: 1.2rem;
    border-radius: 10px;
    margin-bottom: 1.5rem;
}
.result {
    background-color: #d8c9f3;
    color: #222;
    padding: 1rem;
    border-radius: 10px;
    text-align: center;
    font-weight: 600;
}
footer {
    text-align: center;
    margin-top: 2rem;
    font-size: 0.9rem;
    color: #777;
}
.sticky-cta {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #5a2ca0;
    display: flex;
    justify-content: space-around;
    padding: 10px 0;
    z-index: 9999;
}
.sticky-cta a {
    color: white;
    text-decoration: none;
    font-weight: bold;
    padding: 10px 20px;
    border-radius: 6px;
}
.sticky-cta a:hover {
    background-color: #6b3ecf;
}
@media (min-width: 768px) {
    .sticky-cta { display: none; }
}
</style>
""", unsafe_allow_html=True)

# --- Top Section ---
st.title("💇‍♀️ Hvad er en ny kunde egentlig værd for din salon?")
st.markdown("""
Mange bliver overraskede over, **hvor meget én kunde faktisk er værd** for deres salon over tid.  
Denne beregner hjælper dig med at få indsigt i dine kunders **livstidsværdi (CLV)** – opdelt i dame-, herre- og børnekunder.
""")

# --- Function for calculation ---
def calc_clv(price, product, visits, years, new_customers, conversion):
    retained = new_customers * conversion / 100
    total_first_visits = new_customers
    total_revenue = (total_first_visits * (price + product)) + (retained * (price + product) * (visits - 1) * years)
    return total_revenue

# --- Input sections ---
st.header("💰 Damekunder")
with st.container():
    d_new = st.number_input("Antal nye kunder", min_value=0, value=1, step=1, key="d_new")
    d_price = st.number_input("Gennemsnitlig pris pr. besøg (inkl. farve/klip)", min_value=0, value=650, step=50, key="d_price")
    d_prod = st.number_input("Produktsalg pr. besøg", min_value=0, value=75, step=5, key="d_prod")
    d_visits = st.selectbox("Besøg pr. år", [4, 6, 8, 10, 12], index=2, key="d_visits")
    d_years = st.selectbox("Antal år som kunde", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=3, key="d_years")
    d_conv = st.slider("Andel der bliver faste kunder (%)", 0, 100, 50, key="d_conv")

st.header("💇‍♂️ Herrekunder")
with st.container():
    m_new = st.number_input("Antal nye kunder", min_value=0, value=1, step=1, key="m_new")
    m_price = st.number_input("Gennemsnitlig pris pr. besøg", min_value=0, value=400, step=25, key="m_price")
    m_prod = st.number_input("Produktsalg pr. besøg", min_value=0, value=50, step=5, key="m_prod")
    m_visits = st.selectbox("Besøg pr. år", [4, 6, 8, 10, 12], index=3, key="m_visits")
    m_years = st.selectbox("Antal år som kunde", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=2, key="m_years")
    m_conv = st.slider("Andel der bliver faste kunder (%)", 0, 100, 60, key="m_conv")

st.header("🧒 Børnekunder")
with st.container():
    b_new = st.number_input("Antal nye kunder", min_value=0, value=1, step=1, key="b_new")
    b_price = st.number_input("Gennemsnitlig pris pr. besøg", min_value=0, value=300, step=25, key="b_price")
    b_prod = st.number_input("Produktsalg pr. besøg", min_value=0, value=25, step=5, key="b_prod")
    b_visits = st.selectbox("Besøg pr. år", [1, 2, 3, 4, 6], index=2, key="b_visits")
    b_years = st.selectbox("Antal år som kunde", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=3, key="b_years")
    b_conv = st.slider("Andel der bliver faste kunder (%)", 0, 100, 40, key="b_conv")

# --- Calculation ---
if st.button("Beregn livstidsværdi"):
    d_result = calc_clv(d_price, d_prod, d_visits, d_years, d_new, d_conv)
    m_result = calc_clv(m_price, m_prod, m_visits, m_years, m_new, m_conv)
    b_result = calc_clv(b_price, b_prod, b_visits, b_years, b_new, b_conv)
    avg_result = (d_result + m_result + b_result) / 3

    st.subheader("📊 Resultater")
    st.markdown(f"""
    <div class='result'>💇‍♀️ Damekunder: {d_result:,.0f} kr.</div>
    <div class='result'>💇‍♂️ Herrekunder: {m_result:,.0f} kr.</div>
    <div class='result'>🧒 Børnekunder: {b_result:,.0f} kr.</div>
    <div class='result' style='background-color:#bca7f5;'>📈 Gennemsnitlig livstidsværdi: {avg_result:,.0f} kr.</div>
    """, unsafe_allow_html=True)

# --- CTA Section ---
st.markdown("---")
st.subheader("Ønsker du flere kunder?")
st.markdown("""
Vil du vide, **hvor meget dine kunder faktisk er værd?**

Denne beregner viser, hvorfor **løbende nye kunder er forskellen på vækst og stilstand.**  

Jeg hjælper **selvstændige frisører med at skabe vækst** – **uden at miste friheden eller glæden ved faget.**  

Med **16 års erfaring fra marketing** og som **tidligere partner i en frisørsalon**, får du en sparringspartner, der forstår din hverdag og ved, hvordan du får **styr på både kunder, strategi og bundlinje.**

👉 [**Book 20 min. gratis sparring**](https://www.klary.dk)  
🔗 [**Besøg min LinkedIn-profil**](https://www.linkedin.com/in/michael-christensen-dk/)  
📞 [**Ring nu: 28 10 96 68**](tel:+4528109668)
""")

# --- Footer ---
st.markdown("""
<footer>
Powered by <a href="https://www.klary.dk" target="_blank">Klary.dk</a> – Uvildig marketingrådgivning
</footer>
""", unsafe_allow_html=True)

# --- Sticky CTA (mobil only) ---
st.markdown("""
<div class="sticky-cta">
  <a href="https://www.klary.dk" target="_blank">📅 Book sparring</a>
  <a href="tel:+4528109668">📞 Ring nu</a>
</div>
""", unsafe_allow_html=True)


