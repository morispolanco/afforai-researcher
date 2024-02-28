import streamlit as st
import requests

# Función para realizar la solicitud a la API
def get_completion_result(api_key, session_id, content, powerful, google):
    url = "https://api.afforai.com/api/api_completion"
    payload = {
        "apiKey": api_key,
        "sessionID": session_id,
        "history": [{"role": "user", "content": content}],
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

# Valores predeterminados para la API Key y Session ID
default_api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
default_session_id = "65489d7c9ad727940f2ab26f"

# Definir parámetros de entrada
content = st.text_area('Content', height=150)
powerful = st.checkbox('Powerful')
google = st.checkbox('Google')

# Si se ha proporcionado una API Key y un Session ID, mostrar el botón "Obtener Respuesta"
if st.button('Obtener Respuesta'):
    # Realizar la solicitud a la API utilizando los valores predeterminados
    result = get_completion_result(default_api_key, default_session_id, content, powerful, google)

    # Mostrar el resultado formateado si está disponible
    if result:
        st.markdown('### Resultado:')
        for key, value in result.items():
            st.markdown(f"**{key}:** {value}<br>", unsafe_allow_html=True)
    else:
        st.write('Error: Failed to fetch result from the API')
