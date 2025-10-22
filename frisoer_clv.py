import streamlit as st

st.set_page_config(page_title="CLV-beregner for frisører", page_icon="💇‍♀️", layout="centered")

st.title("💇‍♀️ CLV-beregner for frisører")
st.write("Beregn hvor meget en gennemsnitlig kunde er værd for din salon – og se hvordan små ændringer påvirker din indtjening i realtid.")

st.divider()
st.header("👩 Damekunder")

d_clip = st.number_input("Pris for dameklip (kr.)", 0, 5000, 600)
d_color = st.number_input("Pris for farvning (kr.)", 0, 5000, 750)
d_stripe = st.number_input("Pris for striber/highlights (kr.)", 0, 5000, 950)
d_color_share = st.slider("Andel kunder der får farve (%)", 0, 100, 60)
d_stripe_share = st.slider("Andel kunder der får striber (%)", 0, 100, 40)
d_prod = st.number_input("Produktsalg pr. damebesøg (kr.)", 0, 2000, 100)
d_visits = st.slider("Besøg pr. år (dame)", 1, 12, 6)
d_years = st.slider("Antal år som kunde (dame)", 1, 10, 3)
d_close = st.slider("Faste kunder ud af 10 nye (dame)", 0, 10, 7)

d_service = d_clip + d_color*(d_color_share/100) + d_stripe*(d_stripe_share/100)
d_clv = ((d_service + d_prod) * d_visits * d_years) * (d_close/10)

st.metric("💇‍♀️ Damekunde – livstidsværdi", f"{d_clv:,.0f} kr.".replace(",", "."))

st.divider()
st.header("👨 Herrekunder")

m_clip = st.number_input("Pris for herreklip (kr.)", 0, 5000, 400)
m_prod = st.number_input("Produktsalg pr. herrebesøg (kr.)", 0, 2000, 50)
m_visits = st.slider("Besøg pr. år (herre)", 1, 12, 8)
m_years = st.slider("Antal år som kunde (herre)", 1, 10, 3)
m_close = st.slider("Faste kunder ud af 10 nye (herre)", 0, 10, 6)

m_service = m_clip
m_clv = ((m_service + m_prod) * m_visits * m_years) * (m_close/10)

st.metric("💇‍♂️ Herrekunde – livstidsværdi", f"{m_clv:,.0f} kr.".replace(",", "."))

st.divider()
st.header("👶 Børnekunder")

b_clip = st.number_input("Pris for børneklip (kr.)", 0, 5000, 300)
b_prod = st.number_input("Produktsalg pr. børnebesøg (kr.)", 0, 2000, 0)
b_visits = st.slider("Besøg pr. år (børn)", 1, 12, 2)
b_years = st.slider("Antal år som kunde (børn)", 1, 10, 2)
b_close = st.slider("Faste kunder ud af 10 nye (børn)", 0, 10, 5)

b_service = b_clip
b_clv = ((b_service + b_prod) * b_visits * b_years) * (b_close/10)

st.metric("👶 Børnekunde – livstidsværdi", f"{b_clv:,.0f} kr.".replace(",", "."))

avg = round((d_clv + m_clv + b_clv) / 3)

st.divider()
st.subheader("📊 Gennemsnitlig kundeværdi")
st.metric("Gennemsnitlig livstidsværdi", f"{avg:,.0f} kr.".replace(",", "."))

st.caption("Beregningen tager højde for priser, produktsalg, besøg, kundevarighed og din lukkerate (faste kunder ud af 10 nye).")

st.markdown("""
---
### Ønsker du flere kunder – uden bureaukaos?
Jeg er uvildig rådgiver med 16+ års erfaring og hjælper selvstændige med at skabe vækst gennem klarhed og kontrol.

👉 [Besøg min LinkedIn](https://www.linkedin.com/)  
👉 [Book gratis møde på Klary.dk](https://www.klary.dk)
""")
