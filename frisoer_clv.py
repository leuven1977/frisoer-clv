import streamlit as st

st.set_page_config(page_title="Kundeværdi-beregner for frisører", layout="centered")

# --- TOP TEKST ---
st.title("💇‍♀️ Hvad er en ny kunde egentlig værd for din salon?")
st.write("""
Denne beregner er skabt for at vise frisører, **hvor vigtig en enkelt kunde egentlig er** – og hvorfor løbende nye kunder er nøglen til vækst.

Jeg hjælper selvstændige frisører, med at skabe vækst. **Resultatet – en hverdag med mere frihed og en bedre løn.**

Med 16 års erfaring i marketing og som tidligere partner i en frisørsalon, hjælper jeg dig med at få **ro i maven og styr på salonen.**
""")

st.divider()

# --- FUNKTION TIL BEREGNING ---
def calc_clv(new_customers, price, products, visits, years, color_share, color_freq, include_color=True):
    # Undgå beregning for 0 kunder
    if new_customers <= 0:
        return 0, 0

    # Beregn farve/striber ekstra omsætning (kun hvis der vælges noget)
    color_add = 0
    if include_color and new_customers > 5 and color_freq != "Ingen":
        freq_map = {
            "Hver 2. gang": 0.5,
            "Hver 3. gang": 1/3,
            "Hver 4. gang": 0.25,
            "Hver 5. gang": 0.2
        }
        color_add = price * freq_map[color_freq] * (color_share / 100)

    annual_value = (price + products + color_add) * visits
    clv_per_customer = annual_value * years
    total_clv = clv_per_customer * new_customers
    return clv_per_customer, total_clv


# --- DAME SEKTION ---
st.header("💰 Damekunder")
with st.container():
    d_new = st.number_input("Antal nye kunder", min_value=0, value=1, step=1)
    d_price = st.number_input("Gennemsnitlig pris pr. besøg", min_value=0, value=650, step=50)
    d_prod = st.number_input("Produktsalg pr. besøg", min_value=0, value=0, step=10)
    d_color_share = st.selectbox("Hvor mange af dine damekunder får farve eller striber?", ["Ingen", "Hver 2. kunde", "Hver 3. kunde", "Hver 4. kunde", "Hver 5. kunde"], index=0)
    d_color_freq = st.selectbox("Hvor ofte får dine farvekunder i gennemsnit farve/striber?", ["Ingen", "Hver 2. gang", "Hver 3. gang", "Hver 4. gang", "Hver 5. gang"], index=0)
    d_visits = st.selectbox("Besøg pr. år", [4, 6, 8, 10, 12], index=2)
    d_years = st.selectbox("Gennemsnitligt antal år som kunde", [1,2,3,4,5,6,7,8,9,10], index=4)

# Konverter "Hver X kunde" til %
share_map = {"Ingen": 0, "Hver 2. kunde": 50, "Hver 3. kunde": 33, "Hver 4. kunde": 25, "Hver 5. kunde": 20}
color_share_value = share_map[d_color_share]

d_clv_per, d_total = calc_clv(d_new, d_price, d_prod, d_visits, d_years, color_share_value, d_color_freq, include_color=True)

st.info(f"**Værdi pr. damekunde (gennemsnit):** {int(d_clv_per):,} kr.".replace(",", "."))
st.success(f"**Samlet livstidsværdi for damekunder:** {int(d_total):,} kr.".replace(",", "."))

st.divider()

# --- HERRE SEKTION ---
st.header("💈 Herrekunder")
with st.container():
    m_new = st.number_input("Antal nye kunder", min_value=0, value=1, step=1)
    m_price = st.number_input("Gennemsnitlig pris pr. besøg", min_value=0, value=350, step=25)
    m_prod = st.number_input("Produktsalg pr. besøg", min_value=0, value=0, step=10)
    m_visits = st.selectbox("Besøg pr. år", [4,6,8,10,12], index=2)
    m_years = st.selectbox("Gennemsnitligt antal år som kunde", [1,2,3,4,5,6,7,8,9,10], index=4)

m_clv_per, m_total = calc_clv(m_new, m_price, m_prod, m_visits, m_years, 0, "Ingen", include_color=False)

st.info(f"**Værdi pr. herrekunde (gennemsnit):** {int(m_clv_per):,} kr.".replace(",", "."))
st.success(f"**Samlet livstidsværdi for herrekunder:** {int(m_total):,} kr.".replace(",", "."))

st.divider()

# --- BØRNE SEKTION ---
st.header("🧒 Børnekunder")
with st.container():
    b_new = st.number_input("Antal nye kunder", min_value=0, value=1, step=1)
    b_price = st.number_input("Gennemsnitlig pris pr. besøg", min_value=0, value=250, step=25)
    b_prod = st.number_input("Produktsalg pr. besøg", min_value=0, value=0, step=10)
    b_visits = st.selectbox("Besøg pr. år", [1,2,3,4,5,6,8,10], index=2)
    b_years = st.selectbox("Gennemsnitligt antal år som kunde", [1,2,3,4,5,6,7,8,9,10], index=4)

b_clv_per, b_total = calc_clv(b_new, b_price, b_prod, b_visits, b_years, 0, "Ingen", include_color=False)

st.info(f"**Værdi pr. børnekunde (gennemsnit):** {int(b_clv_per):,} kr.".replace(",", "."))
st.success(f"**Samlet livstidsværdi for børnekunder:** {int(b_total):,} kr.".replace(",", "."))

st.divider()

# --- SAMLET VÆRDI ---
total_all = d_total + m_total + b_total
st.header("📊 Samlet værdi for alle kunder")
st.success(f"**Samlet livstidsværdi for salonen:** {int(total_all):,} kr.".replace(",", "."))

st.divider()

# --- BUNDSEKTION ---
st.write("""
### 🧭 Ønsker du flere loyale kunder – uden at miste overblikket?
Beregneren er skabt udelukkende for at hjælpe frisører med at få øjnene op for, hvor vigtig kundeloyalitet er for vækst.  
Jeg hjælper frisører, der har mistet tilliden til bureauer, med at skabe en forretning med **fokus på strategi, vækst og frihed**.

👉 **Book et gratis møde på [Klary.dk](https://www.klary.dk)**  
🔗 **Besøg min [LinkedIn-profil](https://www.linkedin.com/in/michael-christensen-dk/)**  
📞 **Ring direkte på 28 10 96 68**
""")
