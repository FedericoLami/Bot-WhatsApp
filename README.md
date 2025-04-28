Bot de WhatsApp para Agendar Eventos en Google Calendar
Este proyecto es un bot de WhatsApp de prueba que permite recibir mensajes y procesarlos para eventualmente agendar eventos en Google Calendar.
El objetivo principal fue aprender a conectar Flask + Twilio + Google Cloud OAuth de forma básica.

Tecnologías utilizadas
Python 3

Flask

Twilio API for WhatsApp

Ngrok

Google Cloud Console (OAuth 2.0)

Pasos que seguí
1. Configuración inicial
Creé un entorno virtual en Linux (python3 -m venv venv) y lo activé.

Instalé Flask y Twilio en el entorno virtual (pip install flask twilio).

2. Creación del bot en Flask
Creé el archivo app.py con una ruta /whatsapp que recibe mensajes de WhatsApp.

El bot simplemente devuelve un mensaje reconociendo lo que el usuario escribió.

python
Copiar
Editar
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    msg.body(f"Recibí tu mensaje: {incoming_msg}")

    return str(resp)

if __name__ == '__main__':
    app.run(port=5000)
3. Exposición local con Ngrok
Instalé ngrok.

Ejecuté ngrok http 5000 para generar un dominio público que redirige a mi servidor local de Flask.

4. Configuración de Twilio Sandbox para WhatsApp
Me registré en Twilio y configuré el sandbox de WhatsApp.

En el Sandbox de Twilio, configuré el Webhook URL apuntando a mi dominio de ngrok más /whatsapp, por ejemplo:

bash
Copiar
Editar
https://a17c-181-169-243-164.ngrok-free.app/whatsapp
Probé enviando mensajes de WhatsApp al número del sandbox y recibí respuestas automáticas del bot.

5. Creación de proyecto en Google Cloud Console
Creé un proyecto nuevo.

Configuré la pantalla de consentimiento de OAuth con los datos básicos (nombre de la app y contacto).

Creé un ID de Cliente OAuth 2.0 del tipo Aplicación Web.

Agregué como URL de redirección autorizada la dirección de ngrok más /callback, por ejemplo:

bash
Copiar
Editar
https://a17c-181-169-243-164.ngrok-free.app/callback
Guardé las credenciales para utilizarlas más adelante en la integración con Google Calendar.
