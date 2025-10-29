# --- Input sections ---

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
        # beregn frekvensfaktor for farve/striber
        freq_map = {"Hver gang": 1.0, "Hver 2. gang": 0.5, "Hver 3. gang": 1/3, "Hver 4. gang": 0.25, "Aldrig": 0.0}
        color_factor = freq_map[d_color_freq]
        d_total = d_new * ((d_price + (d_color * color_factor) + d_prod) * d_visits * d_years)
        st.success(f"💇‍♀️ Estimeret livstidsværdi for damekunder: {int(d_total):,} kr.".replace(",", "."))


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
