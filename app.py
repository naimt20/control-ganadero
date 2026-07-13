# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:36:33 2026

@author: jaken
"""
import streamlit as st
import os
from data_manager import DataHandler

st.set_page_config(page_title="Control Ganadero OS", layout="wide")

# Estilos
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #e0e0e0; }
    label { color: #66bb6a !important; font-weight: bold; }
    .stButton>button { background: linear-gradient(90deg, #2e7d32, #66bb6a); color: white; border: none; border-radius: 20px; }
    h1 { color: #66bb6a !important; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

# Logo y Título
st.sidebar.title("📍 Menú de Control")
if os.path.exists("ganado.png"): st.sidebar.image("ganado.png", width=150)

opcion = st.sidebar.radio("Sección:", ["Inventario", "Ventas", "Pagos_Detalle", "Clientes"])

col1, col2 = st.columns([1, 6])
with col1:
    if os.path.exists("ganado.png"): st.image("ganado.png", width=100)
with col2:
    st.title(f"Gestión de {opcion}")

# Conexión a BD
db = DataHandler('credenciales.json', '11bseSAQ565xrs-VSUgb3g8UdAo7qpTPBqPqTF6ktn1k')

# Lógica
if opcion == "Inventario":
    with st.form("inv_form"):
        col1, col2 = st.columns(2)
        id_a = col1.text_input("ID_Animal")
        f_e = col1.date_input("Fecha_Entrada")
        lote = col2.text_input("Lote")
        costo = col2.number_input("Costo")
        estado = col2.selectbox("Estado", ["En Finca", "Vendido", "Enfermo", "Rechazado"])
        if st.form_submit_button("Guardar"):
            db.add_record('Inventario', [id_a, str(f_e), lote, costo, estado])
            st.success("Guardado")

elif opcion == "Ventas":
    with st.form("venta_form"):
        col1, col2 = st.columns(2)
        id_v = col1.text_input("ID_Venta")
        fecha = col1.date_input("Fecha")
        id_a = col2.text_input("ID_Animal")
        cliente = col2.text_input("Cliente")
        total = col1.number_input("Total_Venta")
        pagado = col1.number_input("Total_Pagado")
        if st.form_submit_button("Guardar Venta"):
            saldo = total - pagado
            db.add_record('Ventas', [id_v, str(fecha), id_a, cliente, total, pagado, saldo, "Pendiente"])
            st.success("Venta guardada")

elif opcion == "Pagos_Detalle":
    with st.form("pago_form"):
        id_p = st.text_input("ID_Pago")
        id_v = st.text_input("ID_Venta")
        f_p = st.date_input("Fecha_Pago")
        monto = st.number_input("Monto")
        metodo = st.selectbox("Metodo", ["Efectivo", "Transferencia", "Cheque"])
        if st.form_submit_button("Guardar Pago"):
            db.add_record('Pagos_Detalle', [id_p, id_v, str(f_p), monto, metodo])
            st.success("Pago guardado")

elif opcion == "Clientes":
    with st.form("cliente_form"):
        id_c = st.text_input("ID_Cliente")
        nom = st.text_input("Nombre_Comp")
        tel = st.text_input("Telefono")
        email = st.text_input("Email")
        if st.form_submit_button("Guardar Cliente"):
            db.add_record('Clientes', [id_c, nom, tel, email])
            st.success("Cliente guardado")
