import os
import pickle
import google.auth  # type: ignore
from google_auth_oauthlib.flow import InstalledAppFlow  # type: ignore
from googleapiclient.discovery import build  # type: ignore
from googleapiclicalient.errors import HttpError  # type: ignore
import re
from flask import Flask, request  # type: ignore
from twilio.twiml.messaging_response import MessagingResponse  # type: ignore

# Si modificas estos alcances, elimina el archivo token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']  # type: ignore

def authenticate_google_account():
    """Obtiene las credenciales del usuario de Google."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # type: ignore
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').lower()
    print(f"Mensaje recibido: {incoming_msg}")  # Depuración

    resp = MessagingResponse()
    msg = resp.message()

    # Aquí procesamos el mensaje de entrada, por ejemplo, buscar "evento"
    if 'evento' in incoming_msg:
        # Usamos una expresión regular para capturar la fecha (y opcionalmente la hora)
        match = re.search(r'evento\s+\S+\s+fecha\s+(\d{4}-\d{2}-\d{2})\s*(\d{2}:\d{2})?', incoming_msg)

        if match:
            fecha = match.group(1)  # La fecha encontrada
            hora = match.group(2) if match.group(2) else "00:00"  # Si no hay hora, poner las 00:00
            print(f"Fecha encontrada: {fecha}, Hora encontrada: {hora}")  # Depuración
            msg.body(f"¡Tu evento está agendado para el {fecha} a las {hora}!")
        else:
            msg.body("No pude entender la fecha o la hora. Usa el formato correcto: evento <nombre> fecha <yyyy-mm-dd> <hh:mm>")

    else:
        msg.body(f"Recibí tu mensaje: {incoming_msg}")

    return str(resp)

if __name__ == '__main__':
    app.run(port=5000)
