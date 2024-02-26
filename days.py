import streamlit as st
from datetime import datetime

# Az alkalmazás címe
st.title("Napok és Hónapok Számlálója")

# A kapcsolat kezdete
kezdet = datetime(2021, 9, 26)
ma = datetime.now()

# Napok száma a kapcsolat kezdete óta
eltelt_napok = (ma - kezdet).days
st.write(f"Már {eltelt_napok} napja együtt vagyunk.")

# Hónapok száma a kapcsolat kezdete óta
eltelt_honapok = (ma.year - kezdet.year) * 12 + ma.month - kezdet.month
st.write(f"Már {eltelt_honapok} hónapja vagyunk együtt.")

# Számolja, hány nap van még júliusig (feltételezve, hogy július 1. a cél)
julius_első = datetime(ma.year, 7, 1)
if ma > julius_első:
    julius_első = datetime(ma.year + 1, 7, 1)
napok_juliusig = (julius_első - ma).days
st.write(f"Már csak {napok_juliusig} nap van hátra júliusig.")

# Kép feltöltése
st.image('randomimage.jpeg')
