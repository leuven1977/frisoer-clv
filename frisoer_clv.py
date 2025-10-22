import streamlit as st

st.set_page_config(page_title="CLV-beregner for frisører", page_icon="💇‍♀️", layout="centered")

st.title("💇‍♀️ CLV-beregner for frisører")
st.write("Beregn hvor meget dine kunder er værd for din salon – og se hvor meget ekstra du kan tjene med nye faste kunder.")

st.divider()

# ---------- Damekunder ----------
st.header("👩 Damekunder")

d_new_customers = st.number_input("Antal nye kunder (kvinder)", min_value=0, value=5, step=1)

d_clip = st.number_input("Pris for dameklip (kr.)", min_value=0, value=600, step=50)
d_color = st.number_input("Pris for farvning (kr.)", min_value=0, value=750, step=50)
d_stripe = st.number_input("Pris for striber/highlights (kr.)", min_value=0, value=950, step=50)

col1, col2 = st.columns(2)
with col1:
    d_color_share = st.selectbox("Andel kunder der får farve (%)", [0, 20, 40, 60, 80, 100], index=3)
with col2:
    d_stripe_share = st.selectbox("Andel kunder der får striber (%)", [0, 20, 40, 60, 80, 100], index=2)

d_prod = st.number_input("Produktsalg pr. damebesøg (kr.)", min_value=0, value=100, step=25)

col3, col4 = st.columns(2)
with col3:
    d_visits = st.selectbox("Besøg pr. år", [1, 2, 4, 6, 8, 10, 12], index=2)
with col4:
    d_years = st.selectbox("Antal år som kunde", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=2)

d_close = st.number_input("Andel faste kunder ud af 10", min_value=0, max_value=10, value=7, step=1)

d_clv = ((d_clip + d_color * (d_color_share / 100) + d_stripe * (d_stripe_share / 100) + d_prod) 
         * d_visits * d_years) * (d_close / 10) * d_new_customers

st.metric("💇‍♀️ Samlet livstidsværdi – Damekunder", f"{d_clv:,.0f} kr.".replace(",", "."))

st.divider()

# ---------- Herrekunder ----------
st.header("👨 Herrekunder")

m_new_customers = st.number_input("Antal nye kunder (mænd)", min_value=0, value=5, step=1)

m_clip = st.number_input("Pris for herreklip (kr.)", min_value=0, value=400, step=25)
m_prod = st.number_input("Produktsalg pr. herrebesøg (kr.)", min_value=0, value=50, step=10)

col5, col6 = st.columns(2)
with col5:
    m_visits = st.selectbox("Besøg pr. år", [1, 2, 4, 6, 8, 10, 12], index=3)
with col6:
    m_years = st.selectbox("Antal år som kunde", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=2)

m_close = st.number_input("Andel faste kunder ud af 10", min_value=0, max_value=10, value=6, step=1)

m_clv = ((m_clip + m_prod) * m_visits * m_years) * (m_close / 10) * m_new_customers

st.metric("💇‍♂️ Samlet livstidsværdi – Herrekunder", f"{m_clv:,.0f} kr.".replace(",", "."))

st.divider()

# ---------- Børnekunder ----------
st.header("👶 Børnekunder")

b_new_customers = st.number_input("Antal nye kunder (børn)", min_value=0, value=5, step=1)

b_clip = st.number_input("Pris for børneklip (kr.)", min_value=0, value=300, step=25)
b_prod = st.number_input("Produktsalg pr. børnebesøg (kr.)", min_value=0, value=0, step=10)

col7, col8 = st.columns(2)
with col7:
    b_visits = st.selectbox("Besøg pr. år", [1, 2, 4, 6, 8, 10, 12], index=1)
with col8:
    b_years = st.selectbox("Antal år som kunde", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=1)

b_close = st.number_input("Andel faste kunder ud af 10", min_value=0, max_value=10, value=5, step=1)

b_clv = ((b_clip + b_prod) * b_visits * b_years) * (b_close / 10) * b_new_customers

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
