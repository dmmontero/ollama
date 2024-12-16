# Ollama

El actual proyecto muestra el uso de Ollama ejecutandose localmente e interactuado con una interfaz desarrolada con streamlit, el código desarrollado está alojaado en el siguiente repositorio:

<https://github.com/dmmontero/ollama.git/>

## Configuración

A continuación explicaremos cómo configurar la herramienta:

Requerimientos necesarios para el funcionamiento:

- Instale Ollama para Windows siguiendo las siguientes instrucciones:
  <https://ollama.com/download/windows>
- Una vez tenga Ollama instalado desde power shell descargue el modelo de 1B de parámetros ejecutando el siguiente comando:
  _ollama run llama3.2:1b_
- Verifique que el modelo se este ejecutando con el comando : _ollama list_

- Abra el Prompt y ejecute las siguientes instrucciones:

1. Crea un ambiente virtual, en nuestro caso usamos la version 3.12.8 de python:
   _python -m venv ollama_

2. Ir a la carpeta del proyecto y activar el ambiente virtual creado:\
   _.\ollama\Scripts\Activate.ps1_

3. Instalar los paquetes definidos para el proyecto:\
   _pip install -r requirements.txt_

4. Ejecutar el proyecto, este comando le permite ver la api en la maquina de desarrollo:\
   _streamlit run .\app.py_

5. Una vez ejecutado el comando podra ver la aplicacion en <http://localhost:8501/> 8501 es el puerto por defecto
