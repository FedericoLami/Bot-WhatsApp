# Bot de WhatsApp para Agendar Eventos en Google Calendar

Este proyecto es un bot básico que recibe mensajes de WhatsApp y responde automáticamente.  
Además, se conecta con Google Calendar para registrar eventos.

## Tecnologías utilizadas

- Python
- Flask
- Twilio Sandbox para WhatsApp
- Ngrok
- API de Google Calendar

## Pasos realizados

1. **Configuración del entorno:**
   - Creación de un entorno virtual en Python.
   - Instalación de las dependencias necesarias (`Flask`, `twilio`).

2. **Configuración de Twilio:**
   - Creación de cuenta gratuita en Twilio.
   - Activación del Sandbox de WhatsApp.
   - Configuración del webhook hacia nuestro servidor local usando ngrok.

3. **Configuración de ngrok:**
   - Instalación de ngrok.
   - Exposición de nuestro servidor Flask local al exterior.

4. **Desarrollo básico del bot:**
   - Creación del archivo `app.py`.
   - Configuración de Flask para recibir y responder mensajes de WhatsApp.

5. **Configuración de Google Cloud:**
   - Creación de proyecto en Google Cloud Console.
   - Configuración de pantalla de consentimiento OAuth.
   - Creación de credenciales OAuth para permitir al bot escribir en Google Calendar.

## Estado del proyecto

✅ El bot recibe mensajes por WhatsApp y responde automáticamente.  
✅ Configurado para integrar eventos con Google Calendar (próxima etapa).

## Cómo correr el proyecto

```bash
# Crear entorno virtual
python3 -m venv venv

# Activarlo
source venv/bin/activate

# Instalar dependencias
pip install Flask twilio

# Ejecutar la app
python app.py
