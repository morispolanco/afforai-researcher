import streamlit as st
import requests

# Función para realizar la solicitud a la API
def get_completion_result(api_key, session_id, history, powerful, google):
    url = "https://api.afforai.com/api/api_completion"
    payload = {
        "apiKey": fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e,
        "sessionID": 65deb80c5b0fa2b25f3216b7,
        "history": history,
        "powerful": powerful,
        "google": google
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Configuración de la aplicación Streamlit
st.title('Afforai API Demo')

# Parámetros de entrada
api_key = st.text_input('API Key')
session_id = st.text_input('Session ID')
role = st.selectbox('Role', ['user', 'assistant'])
content = st.text_input('Content')
powerful = st.checkbox('Powerful')
google = st.checkbox('Google')

history = [{"role": role, "content": content}]

# Si se ha proporcionado una API Key y un Session ID, realizar la solicitud a la API
if st.button('Get Completion'):
    if api_key and session_id:
        result = get_completion_result(api_key, session_id, history, powerful, google)
        if result:
            st.write('Result:')
            st.json(result)
        else:
            st.write('Error: Failed to fetch result from the API')
    else:
        st.write('Please provide API Key and Session ID')
