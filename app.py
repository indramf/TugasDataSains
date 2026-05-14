import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model_mobil.pkl')

st.set_page_config(page_title="Prediksi Harga Mobil", layout="wide")
st.header("PREDIKSI HARGA MOBIL")

col1, col2 = st.columns(2)

with col1:
    st.subheader("INPUT SPESIFIKASI:")
    engine = st.number_input("Variable 1: Engine Size", value=2.0)
    hp = st.number_input("Variable 2: Horsepower", value=150.0)
    wheel = st.number_input("Variable 3: Wheelbase", value=100.0)
    fuel = st.number_input("Variable N: Fuel Capacity", value=15.0)
    
    btn = st.button("Hitung Harga Mobil")

with col2:
    st.subheader("PERKIRAAN HARGA MOBIL")
    if btn:
        input_data = pd.DataFrame([[engine, hp, wheel, fuel]], 
                                  columns=['Engine_size', 'Horsepower', 'Wheelbase', 'Fuel_capacity'])
        hasil = model.predict(input_data)
        st.success(f"### ${hasil[0]:,.3f}")
        st.write(f"Variable 1: {engine}")
        st.write(f"Variable 2: {hp}")
    
    st.info("SISTEM INI DIBUAT OLEH:\nNAMA: INDRA\nNPM: (Isi NPM Kamu)")