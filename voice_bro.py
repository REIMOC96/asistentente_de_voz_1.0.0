import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import asyncio
import pyautogui

# Nombre del asistente virtual
name = "wilson"

# Inicialización de objetos
listener = sr.Recognizer()
engine = pyttsx3.init()

# Número de teléfono para enviar mensajes de WhatsApp
cellphone = ""

#quiero hacer una base de datos para tener mis contactos y tratar de llamarlos segun el nombre


# Configuración de la voz del asistente
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Variable para controlar la ejecución del programa
running = True

# Función para que el sistema hable
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Función para escuchar la entrada de voz
def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return ""
    except sr.RequestError as e:
        print(f"Error en la solicitud de reconocimiento de voz: {e}")
        return ""
    return rec

# Función para enviar mensaje de WhatsApp de forma asíncrona
async def send_whatsapp_message_async(msj):
    hora_actual = datetime.datetime.now()
    pywhatkit.sendwhatmsg(cellphone, msj, hora_actual.hour, hora_actual.minute + 1)
    talk("Mensaje enviado: " + msj)

# Función principal para ejecutar el asistente de forma asíncrona
async def run_wilson():
    global running  # Usamos la variable global
    
    while running:  # Bucle infinito para escuchar continuamente
        rec = listen()
        
        # Reproduce música en YouTube
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo " + music)
            pywhatkit.playonyt(music)
            talk("Reproduciendo " + music)
        
        elif 'pausa' in rec:
            print("pausando")
            talk("pausando la reproduccion")
            pyautogui.hotkey('fn', 'f7')
        
        # Envia mensaje de WhatsApp de forma asíncrona
        elif 'mensaje' in rec and 'envía' in rec:
            msj = rec.replace('mensaje', ''), rec.replace('envía', '')
            print("Mensaje", msj)
            
            # Inicia la tarea asíncrona para enviar el mensaje
            await send_whatsapp_message_async(msj)
        
        # Realiza búsqueda en Google
        elif 'busca' in rec:
            src = rec.replace('busca', '')
            print("Buscando", src, "en Google")
            pywhatkit.search(src)
            talk("Buscando en Google: " + src)
        
        # Comando para detener la ejecución
        elif 'detener' in rec:
            talk("Deteniendo el programa")
            running = False

        #pedir la hora desde aqui: 
        
        #limpiador de archios 
        
        #organizador de descargas
        
        #organizador de carpetas de desarrollo (esta es dificil)
        
        #SACAR SREENSHOT, DE PROGRAMA O DE PANTALLA, PREFERENTE AMBOS
        
        # enviar mensajes por discord (ta brijido)         

        #ingresar a canal de discord, y enviar mensaje por canal de txt
        
        #llamar por discord
        
        #crear aechivos y sus extensiones
        
        #crear carpetas

# Verifica si el script se está ejecutando como programa principal
if __name__ == '__main__':
    asyncio.run(run_wilson())
