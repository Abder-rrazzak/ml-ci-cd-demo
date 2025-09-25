import streamlit as st
import requests

# URL de ton API FastAPI sur Render
API_URL = "https://ml-ci-cd-demo-2.onrender.com/predict"

label_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

st.set_page_config(page_title="Prédicteur Iris 🌸", page_icon="🌸")
st.title("🌸 Prédicteur de fleurs Iris")
st.markdown("Entrez les caractéristiques de la fleur pour obtenir une prédiction.")

# Formulaire utilisateur
sepal_length = st.number_input("Longueur du sépale (cm)", min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input("Largeur du sépale (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input("Longueur du pétale (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input("Largeur du pétale (cm)", min_value=0.0, max_value=10.0, step=0.1)

if st.button("🔍 Prédire"):
    features = [sepal_length, sepal_width, petal_length, petal_width]
    payload = {"features": features}

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        prediction_index = response.json()["prediction"][0]
        flower_name = label_names[prediction_index]
        st.success(f"🌼 Prédiction : **{flower_name}**")
    except Exception as e:
        st.error(f"Erreur lors de la requête : {e}")
