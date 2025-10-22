import streamlit as st

st.set_page_config(page_title="CLV-beregner for frisører", page_icon="💇‍♀️", layout="centered")

st.title("💇‍♀️ CLV-beregner for frisører")
st.write("Beregn hvor meget dine kunder er værd for din salon – og se hvor meget ekstra du kan tjene med nye faste kunder.")

st.divider()

# ---------- Damekunder ----------
st.header("👩 Damekunder")

d_new_customers = st.number_input("Antal nye kunder (kvinder)", min_value=0, value=5, step=1, key="d_new_customers")

d_clip = st.number_input("Pris for dameklip (kr.)", min_value=0, value=600, step=50, key="d_clip")
d_color = st.number_input("Pris for farvning (kr.)", min_value=0, value=750, step=50, key="d_color")
d_stripe = st.number_input("Pris for striber/highlights (kr.)", min_value=0, value=950, step=50, key="d_stripe")

col1, col2 = st.columns(2)
with col1:
    d_color_share = st.selectbox("Andel kunder der får farve (%)", [0, 20, 40, 60, 80, 100], index=3, key="d_color_share")
with col2:
    d_stripe_share = st.selectbox("Andel kunder der får striber (%)", [0, 20, 40, 60, 80, 100], index=2, key="d_stripe_share")

d_prod = st.number_input("Produktsalg pr. damebesøg (kr.)", min_value=0, value=100, step=25, key="d_prod")

col3, col4 = st.columns(2)
with col3:
    d_visits = st.selectbox("Besøg pr. år", [1, 2, 4, 6, 8, 10, 12], index=2, key="d_visits")
with col4:
    d_years = st.selectbox("Antal år som kunde", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=2, key="d_years")

d_close = st.number_input("Andel faste kunder ud af 10", min_value=0, max_value=10, value=7, step=1, key="d_close")

# Udregning af værdier
d_avg_visit = d_clip + (d_color * (d_color_share / 100)) + (d_stripe * (d_stripe_share / 100)) + d_prod
d_loyal = (d_close / 10) * d_new_customers
d_one_time = d_new_customers - d_loyal
d_clv = (d_loyal * d_avg_visit * d_visits * d_years) + (d_one_time * d_avg_visit)

st.metric("💇‍♀️ Samlet livstidsværdi – Damekunder", f"{d_clv:,.0f} kr.".replace(",", "."))

st.divider()

# ---------- Herrekunder ----------
st.header("👨 Herrekunder")

m_new_customers = st.number_input("Antal nye kunder (mænd)", min_value=0, value=5, step=1, key="m_new_customers")

m_clip = st.number_input("Pris for herreklip (kr.)", min_value=0, value=400, step=25, key="m_clip")
m_prod = st.number_input("Produktsalg pr. herrebesøg (kr.)", min_value=0, value=50, step=10, key="m_prod")

col5, col6 = st.columns(2)
with col5:
    m_visits = st.selectbox("Besøg pr. år", [1, 2, 4, 6, 8, 10, 12], index=3, key="m_visits")
with col6:
    m_years = st.selectbox("Antal år som kunde", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=2, key="m_years")

m_close = st.number_input("Andel faste kunder ud af 10", min_value=0, max_value=10, value=6, step=1, key="m_close")

m_avg_visit = m_clip + m_prod
m_loyal = (m_close / 10) * m_new_customers
m_one_time = m_new_customers - m_loyal
m_clv = (m_loyal * m_avg_visit * m_visits * m_years) + (m_one_time * m_avg_visit)

st.metric("💇‍♂️ Samlet livstidsværdi – Herrekunder", f"{m_clv:,.0f} kr.".replace(",", "."))

st.divider()

# ---------- Børnekunder ----------
st.header("👶 Børnekunder")

b_new_customers = st.number_input("Antal nye kunder (børn)", min_value=0, value=5, step=1, key="b_new_customers")

b_clip = st.number_input("Pris for børneklip (kr.)", min_value=0, value=300, step=25, key="b_clip")
b_prod = st.number_input("Produktsalg pr. børnebesøg (kr.)", min_value=0, value=0, step=10, key="b_prod")

col7, col8 = st.columns(2)
with col7:
    b_visits = st.selectbox("Besøg pr. år", [1, 2, 4, 6, 8, 10, 12], index=1, key="b_visits")
with col8:
    b_years = st.selectbox("Antal år som kunde", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=1, key="b_years")

b_close = st.number_input("Andel faste kunder ud af 10", min_value=0, max_value=10, value=5, step=1, key="b_close")

b_avg_visit = b_clip + b_prod
b_loyal = (b_close / 10) * b_new_customers
b_one_time = b_new_customers - b_loyal
b_clv = (b_loyal * b_avg_visit * b_visits * b_years) + (b_one_time * b_avg_visit)

st.metric("👶 Samlet livstidsværdi – Børnekunder", f"{b_clv:,.0f} kr.".replace(",", "."))

# ---------- Total ----------
total_clv = d_clv + m_clv + b_clv
st.divider()
st.subheader("📊 Samlet livstidsværdi for nye kunder")
st.metric("Samlet potentiel værdi", f"{total_clv:,.0f} kr.".replace(",", "."))

st.divider()
st.write("💡 *Se hvor meget ekstra du kan tjene ved blot få nye faste kunder.*")

st.markdown("""
---
### Ønsker du at forstå, hvor dine marketingkroner gør mest gavn?
Jeg hjælper frisører med at skabe klarhed i samarbejdet med bureauer og få mere ud af deres eksisterende marketing.

👉 [Book et gratis, uforpligtende møde på Klary.dk](https://www.klary.dk)  
🔗 [Se min LinkedIn-profil](https://www.linkedin.com/in/michael-christensen-dk/)  
📞 Ring direkte: **28 10 96 68**
---
""")
