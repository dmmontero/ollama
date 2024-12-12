import streamlit as st
from ollama import chat


# Función para obtener respuesta de ollama.chat
def obtener_respuesta_ollama(input_text):
    response = chat(
        model="llama3.2:1b", messages=[{"role": "user", "content": input_text}]
    )
    return response["message"]["content"]


# Título de la aplicación
st.title(":speak_no_evil: Chat con Ollama")

# Inicializar el valor del campo de texto en session_state
# if "text_input" not in st.session_state:
#     st.session_state.text_input = ""

# # Crear el campo de texto utilizando session_state
# user_input = st.text_input(
#     "Ingresa texto:", value=st.session_state.text_input, key="input_text"
# )


# # Crear un botón para enviar la pregunta
# if st.button("Enviar"):
#     respuesta = obtener_respuesta_ollama(user_input)
#     # Mostrar la respuesta en un área de texto
#     st.text_area("Respuesta de Ollama:", value=respuesta, height=200)

# # Crear un botón para resetear el formulario
# if st.button("Resetear"):
#     st.session_state.text_input = ""  # Resetear el valor en session_state
#     st.rerun()


form = st.form(
    key="ollama-form", clear_on_submit=True, enter_to_submit=True, border=True
)
pregunta = form.text_input("Ingresa pregunta:")
submit = form.form_submit_button("enviar")
st.write(" :outbox_tray: Presione enviar para recibir su respuesta")
if submit:

    with st.spinner(f"Procesando... :surfer: {pregunta}"):
        respuesta = obtener_respuesta_ollama(pregunta)
        # Mostrar la respuesta en un área de texto
        # st.write(f"Pregunta:\n {pregunta} \n Respuesta:\n {respuesta}")
        st.markdown(
            f"""
                :question: :blue-background[Pregunta]: {pregunta}
                </br>
                </br>
                :speaking_head_in_silhouette: :green-background[Respuesta]: {respuesta}
            """,
            unsafe_allow_html=True,
        )
        st.success("Hecho!")
