import streamlit as st

st.set_page_config(page_title="Frisørens kundeværdi-beregner", page_icon="💇‍♀️", layout="centered")

# --- Titel & intro ---
st.title("💇‍♀️ Hvad er en ny kunde egentlig værd for din salon?")
st.write("""
Mange bliver overraskede over, hvor meget **én kunde faktisk er værd** for deres salon.
Denne beregner viser, hvorfor **løbende nye kunder er nøglen til vækst** – og hvor meget de betyder på sigt.
""")

st.divider()

# --- DAMEKUNDER ---
st.subheader("💇‍♀️ Damekunder")
f_customers = st.number_input("Antal nye damekunder", min_value=0, value=20)
col1, col2 = st.columns(2)
with col1:
    f_haircut = st.number_input("Pris på dameklip", min_value=0, value=500)
    f_color = st.number_input("Pris på farve", min_value=0, value=600)
with col2:
    f_highlights = st.number_input("Pris på striber/highlights", min_value=0, value=700)
    f_product = st.number_input("Produktsalg pr. besøg", min_value=0, value=150)

f_color_freq = st.selectbox(
    "Hvor ofte får kunden farve eller striber?",
    ["Hver gang", "Hver 2. gang", "Hver 3. gang", "Hver 4. gang", "Aldrig"],
    index=1
)
col1, col2 = st.columns(2)
with col1:
    f_visits_per_year = st.selectbox("Besøg pr. år", [4, 6, 8, 10, 12], index=2)
with col2:
    f_years = st.selectbox("Antal år som kunde", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=2)

# Frekvensfaktor
freq_map = {"Hver gang": 1, "Hver 2. gang": 0.5, "Hver 3. gang": 1/3, "Hver 4. gang": 0.25, "Aldrig": 0}
color_factor = freq_map[f_color_freq]

if st.button("Beregn damekundeværdi 💇‍♀️"):
    f_service_total = f_haircut + ((f_color + f_highlights) * color_factor)
    f_clv = (f_service_total + f_product) * f_visits_per_year * f_years * f_customers
    st.success(f"💰 Samlet værdi for damekunder: **{f_clv:,.0f} kr.**")
else:
    f_clv = 0

st.divider()

# --- HERREKUNDER ---
st.subheader("💇‍♂️ Herrekunder")
m_customers = st.number_input("Antal nye herrekunder", min_value=0, value=10)
col1, col2 = st.columns(2)
with col1:
    m_haircut = st.number_input("Pris på herreklip", min_value=0, value=350)
with col2:
    m_product = st.number_input("Produktsalg pr. besøg", min_value=0, value=75)

col1, col2 = st.columns(2)
with col1:
    m_visits_per_year = st.selectbox("Besøg pr. år", [6, 8, 10, 12], index=2)
with col2:
    m_years = st.selectbox("Antal år som kunde", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=3)

if st.button("Beregn herrekundeværdi 💇‍♂️"):
    m_clv = (m_haircut + m_product) * m_visits_per_year * m_years * m_customers
    st.success(f"💰 Samlet værdi for herrekunder: **{m_clv:,.0f} kr.**")
else:
    m_clv = 0

st.divider()

# --- BØRNEKUNDER ---
st.subheader("🧒 Børnekunder")
b_customers = st.number_input("Antal nye børnekunder", min_value=0, value=5)
col1, col2 = st.columns(2)
with col1:
    b_haircut = st.number_input("Pris på børneklip", min_value=0, value=250)
with col2:
    b_product = st.number_input("Produktsalg pr. besøg", min_value=0, value=50)

col1, col2 = st.columns(2)
with col1:
    b_visits_per_year = st.selectbox("Besøg pr. år", [2, 3, 4, 5, 6], index=2)
with col2:
    b_years = st.selectbox("Antal år som kunde", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=3)

if st.button("Beregn børnekundeværdi 🧒"):
    b_clv = (b_haircut + b_product) * b_visits_per_year * b_years * b_customers
    st.success(f"💰 Samlet værdi for børnekunder: **{b_clv:,.0f} kr.**")
else:
    b_clv = 0

st.divider()

# --- SAMLET BEREGNING ---
if st.button("📊 Se samlet potentiale for salonen"):
    total_clv = f_clv + m_clv + b_clv
    st.success(f"📈 Samlet potentiel livstidsværdi: **{total_clv:,.0f} kr.**")

st.divider()

# --- CTA ---
st.markdown("""
### 🌟 Ønsker du flere loyale kunder – uden at miste overblikket?
Beregneren er skabt for at hjælpe frisører med at forstå, hvor meget én kunde betyder for deres forretning.

Jeg hjælper **selvstændige frisører med at skabe vækst** – **uden at miste friheden eller glæden ved faget.**

Med **16 års erfaring fra marketing** og som **tidligere partner i en frisørsalon**, får du en sparringspartner, der forstår din hverdag – og ved, hvordan du får **styr på både kunder, strategi og bundlinje.**

👉 [Book et gratis møde på Klary.dk](https://www.klary.dk)  
🔗 [Besøg min LinkedIn-profil](https://www.linkedin.com/in/michael-christensen-dk/)  
📞 Ring direkte på: **28 10 96 68**
""")
