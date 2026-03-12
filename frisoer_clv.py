import streamlit as st

st.set_page_config(page_title="Kundeværdi-beregner for frisører", layout="centered")

# --- TOP TEKST ---
st.title("💇‍♀️ Hvad er én kunde værd for din salon?")  
st.write("""
Hvor meget en kunde er værd, **er et af de vigtigste tal, du skal kende som selvstændig**

Udfyld de tal der bliver efterspurgt, mange bliver overrasket, da de ikke tænker over, hvor meget én kunde egentlig er værd for salonen.  
""")

st.divider()

# --- FUNKTION TIL BEREGNING ---
def calc_clv(new_customers, price, products, visits, years, color_price, color_share_label, color_freq, include_color=True):
    if new_customers <= 0:
        return 0, 0

    # Grundomsætning for alle kunder
    base_total = new_customers * (price + products) * visits * years

    color_total = 0

    if include_color and color_price > 0 and color_share_label != "Ingen" and color_freq != "Ingen":
        share_map = {
            "Hver 2. damekunde": 2,
            "Hver 3. damekunde": 3,
            "Hver 4. damekunde": 4,
            "Hver 5. damekunde": 5
        }

      freq_map = {
    "Hver gang": 1,
    "Hver 2. gang": 0.5,
    "Hver 3. gang": 1/3,
    "Hver 4. gang": 0.25,
    "Hver 5. gang": 0.2
}

        every_nth_customer = share_map.get(color_share_label)
        color_customers = new_customers // every_nth_customer if every_nth_customer else 0
        color_treatments_per_year = visits * freq_map.get(color_freq, 0)

        color_total = color_customers * color_price * color_treatments_per_year * years

    total_clv = base_total + color_total
    clv_per_customer = total_clv / new_customers

    return clv_per_customer, total_clv


# --- DAME SEKTION ---
st.header("💰 Damekunder")
with st.container():
    d_new = st.number_input("Vælg antal nye damekunder du vil beregne", min_value=0, value=1, step=1, key="d_new")
    d_price = st.number_input("Gns. pris for dameklip i din salon", min_value=0, value=550, step=50, key="d_price")
    d_prod = st.number_input("Gns. Produktsalg pr. dame", min_value=0, value=0, step=10, key="d_prod")

    st.subheader("Farve og striber")
    d_color_price = st.number_input("Gns. pris for farve/striber", min_value=0, value=800, step=50, key="d_color_price")
    d_color_share = st.selectbox(
        "Hvor mange af dine damekunder får farve eller striber?",
        ["Ingen", "Hver 2. damekunde", "Hver 3. damekunde", "Hver 4. damekunde", "Hver 5. damekunde"],
        index=0,
        key="d_color_share"
    )
   d_color_freq = st.selectbox(
    "Hvor ofte får dine farvekunder i gns. farve/striber?",
    ["Ingen", "Hver gang", "Hver 2. gang", "Hver 3. gang", "Hver 4. gang", "Hver 5. gang"],
    index=0,
    key="d_color_freq"
)

   d_visits = st.selectbox("Gns. besøg pr. år", [1,2,3,4,5,6,7,8], index=2, key="d_visits")
    d_years = st.selectbox("Gns. antal år som kunde", [1,2,3,4,5,6,7,8,9,10], index=4, key="d_years")

# ✅ Beregning
d_clv_per, d_total = calc_clv(
    d_new,
    d_price,
    d_prod,
    d_visits,
    d_years,
    d_color_price,
    d_color_share,
    d_color_freq,
    include_color=True
)

st.info(f"**Værdi pr. damekunde (gennemsnit):** {int(d_clv_per):,} kr.".replace(",", "."))
st.success(f"**Samlet livstidsværdi for damekunder:** {int(d_total):,} kr.".replace(",", "."))

st.divider()

# --- HERRE SEKTION ---
st.header("💈 Herrekunder")
with st.container():
    m_new = st.number_input("Vælg antal nye herrekunder du vil beregne", min_value=0, value=1, step=1, key="m_new")
    m_price = st.number_input("Gns. pris for herreklip i din salon", min_value=0, value=350, step=25, key="m_price")
    m_prod = st.number_input("Gns. Produktsalg pr. herre", min_value=0, value=0, step=10, key="m_prod")
    m_visits = st.selectbox("Gns. besøg pr. år", [4,6,8,10,12], index=2, key="m_visits")
    m_years = st.selectbox("Gns. antal år som kunde", [1,2,3,4,5,6,7,8,9,10], index=4, key="m_years")

m_clv_per, m_total = calc_clv(m_new, m_price, m_prod, m_visits, m_years, 0, 0, "Ingen", include_color=False)

st.info(f"**Værdi pr. herrekunde (gennemsnit):** {int(m_clv_per):,} kr.".replace(",", "."))
st.success(f"**Samlet livstidsværdi for herrekunder:** {int(m_total):,} kr.".replace(",", "."))

st.divider()

# --- BØRNE SEKTION ---
st.header("🧒 Børnekunder")
with st.container():
    b_new = st.number_input("Vælg antal nye børneklip du vil beregne", min_value=0, value=1, step=1, key="b_new")
    b_price = st.number_input("Gns. pris for børneklip i din salon", min_value=0, value=250, step=25, key="b_price")
    b_prod = st.number_input("Gns. produktsalg pr. barn", min_value=0, value=0, step=10, key="b_prod")
    b_visits = st.selectbox("Gns. besøg pr. år", [1,2,3,4,5,6,8,10], index=2, key="b_visits")
    b_years = st.selectbox("Gns. antal år som kunde", [1,2,3,4,5,6,7,8,9,10], index=4, key="b_years")

b_clv_per, b_total = calc_clv(b_new, b_price, b_prod, b_visits, b_years, 0, 0, "Ingen", include_color=False)

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
### 🧭 Ønsker du frihed og vækst?

Jeg er i dag uvildig rådgiver for frisørere, og hjælper med at skabe vækst og frihed.
Jeg har været selvstændig i 14 år, og har 16 års erfaring i digital marketing og 3 års erfaring med AI.
Vigtigst af alt, jeg skaber overskud og ro i maven for selvstændige.   

Ofte står selvstændige frisører alene med beslutninger, de ikke er klædt på til at tage og det udnytter specielt bureauer.  
Mange har mistet tilliden til bureauer, fordi de har oplevet, at bureauets interesser kommer før deres egne.  

**Regel nr. 1:** Indgå aldrig et samarbejde med et bureau, hvis du ikke selv forstår marketing.  

👉 **Book et gratis møde på [Klary.dk](https://www.klary.dk)**  
🔗 **Besøg min [LinkedIn-profil](https://www.linkedin.com/in/michael-christensen-dk/)**  
📞 **Ring direkte på 28 10 96 68**

Jeg giver altid et gratis sparringsmøde.
""")
























