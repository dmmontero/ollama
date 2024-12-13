# imports
import streamlit as st
from ollama import chat
import httpx


# Función para obtener respuesta de ollama.chat
def obtener_respuesta_ollama(input_text):
    response = chat(
        model="llama3.2:1b", messages=[{"role": "user", "content": input_text}]
    )
    return response["message"]["content"]


# Título de la aplicación
st.title(":speak_no_evil: Chat con Ollama")


# creación formulario
form = st.form(
    key="ollama-form", clear_on_submit=True, enter_to_submit=True, border=True
)
pregunta = form.text_input("Ingresa pregunta:")
submit = form.form_submit_button("enviar")
st.write(" :outbox_tray: Presione enviar para recibir su respuesta")

# Accion a ejecuar cuando se envia el formulario
if submit:
    if not pregunta:
        st.error(":x: Campo obligatorio")
        st.stop()
    try:
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
    except httpx.ConnectError:
        st.error(
            ":no_entry_sign: Ocurrió un error de conexión, verifique que Ollama se este ejecutando"
        )
    except Exception as ex:
        st.error(f":no_entry_sign: Ocurrió un error ejecutando la consulta {type(ex)}")
