import streamlit as st
from modules.chatbot import respond
from modules.vision import analyze_image
from modules.ml_model import predict_value

st.set_page_config(page_title="AI Asistent", layout="centered")
st.title("🤖 AI Asistent pro rozpoznání nálezů")

st.sidebar.header("Modul")
modul = st.sidebar.radio("Vyber funkci:", ["Počítačové vidění", "Chatbot", "Predikce hodnoty"])

if modul == "Počítačové vidění":
    st.header("🖼️ Rozpoznání obrázku (typ mince)")
    uploaded_file = st.file_uploader("Nahraj obrázek mince", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.image(uploaded_file, caption="Nahraný obrázek", use_column_width=True)
        result = analyze_image(uploaded_file)
        st.success(f"Rozpoznaný typ: {result}")

elif modul == "Chatbot":
    st.header("💬 Chat s AI")
    user_input = st.text_input("Napiš dotaz:")
    if user_input:
        answer = respond(user_input)
        st.text_area("Odpověď:", value=answer, height=150)

elif modul == "Predikce hodnoty":
    st.header("📊 Odhad hodnoty nálezu")
    typ = st.selectbox("Typ nálezu:", ["Mince", "Odznak", "Knoflík", "Jiné"])
    stav = st.slider("Stav (1 = špatný, 10 = jako nový):", 1, 10, 5)
    if st.button("Spočítat odhad"):
        value = predict_value(typ, stav)
        st.info(f"Odhadovaná hodnota: {value} Kč")
