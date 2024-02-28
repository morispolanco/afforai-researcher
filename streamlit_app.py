import streamlit as st
import requests
import json

# Define la URL de la API
url = "https://api.afforai.com/api/api_completion"

# Define los headers para la solicitud
headers = {
    "Content-Type": "application/json",
    "apiKey": "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e",
    "sessionID": "65deb80c5b0fa2b25f3216b7"
}

def get_answer(question):
    # Define el cuerpo de la solicitud
    data = {
        "history": [{"role": "user", "content": question}],
        "powerful": True,
        "google": True
    }

    # Realiza la solicitud POST a la API
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Si la solicitud fue exitosa, devuelve la respuesta
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Lo siento, no pude obtener una respuesta."

def main():
    st.title("Aplicación de preguntas y respuestas")

    question = st.text_input("Escribe tu pregunta aquí:")
    if st.button("Obtener respuesta"):
        answer = get_answer(question)
        st.write(answer)

if __name__ == "__main__":
    main()
