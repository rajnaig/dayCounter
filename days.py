import streamlit as st
from datetime import datetime

# Az alkalmazás címe
st.title("Napok Számlálója")

# A kapcsolat kezdete
kezdet = datetime(2021, 9, 26)
ma = datetime.now()

# Napok száma a kapcsolat kezdete óta
eltelt_napok = (ma - kezdet).days
st.write(f"Már {eltelt_napok} napja együtt vagyunk.")

# Számolja, hány nap van még szeptemberig (feltételezve, hogy szeptember 1. a cél)
szeptember_első = datetime(ma.year, 9, 1)
if ma > szeptember_első:
    szeptember_első = datetime(ma.year + 1, 9, 1)
napok_szeptemberig = (szeptember_első - ma).days
st.write(f"Még {napok_szeptemberig} nap van hátra szeptemberig.")

# Egyszerű üzenet
st.write(f"Eddig {eltelt_napok} napot töltöttünk együtt, és már csak {napok_szeptemberig} nap van hátra a közös otthonunkig.")

# Kép feltöltése
st.image('randomimage.jpeg')
