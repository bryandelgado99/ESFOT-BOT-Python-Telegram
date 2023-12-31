import telebot
import threading
from telebot.types import ReplyKeyboardMarkup #Create Buttons
from telebot.types import ForceReply #Create Automatic replays
from telebot.types import ReplyKeyboardRemove
import time
from config import *

#Commands List
commands = ["start", "aulas", "matriculas", "praticas", "vinculacion", "preguntas_frecuentes", "contactos", "regresar"]

#Links and important data
calendario_2023b = '<a href="https://esfot.epn.edu.ec/index.php/esfot/676-calendario-academico-2023-b">Calendario Académico 2023-B</a>' + '\n'
guia_2023b = '<a href="https://esfot.epn.edu.ec/index.php/guia-del-estudiante">Guia del Estudiante 2023-B</a>' + '\n'

#Media
start_img = open("./images/logo2.png", "rb")

#Docs
guia_doc = open("./documents/gu_a_para_el_estudiante_2023-b.pdf", "rb")
calendario_doc = open("./documents/calendario-academico-2023-b_actualizado.pdf", "rb")

#Realases, Titles and Data
important_title = '<b>💁 IMPORTANTE</b>'
advise_title = '<b>⚠ AVISO</b>'
#Major Titles
calendario_title = '<b><u>🗓 Calendario Académico:</u></b>'
guide_title = '<b><u>📑 Guía del Estudiante:</u></b>'
vinculacion_title = '<b><u>👥 Prácticas Comunitarias (Vinculación):</u></b>'
matricula_title = '<b>🎫 Guía de Matriculación</b>'
pasantias_title = '<b><u>🧑‍💼👨‍💼 Prácticas Pre-profesionales y Pasantías:</u></b>'

#Bot Instances and Connection with API
bot = telebot.TeleBot(Telegram_Token)

#Actions and Responses for Bot-----------------------------------------
'''--------- Responses to /Start CMD -----------'''
@bot.message_handler(commands=["start"])
def start_cmd(message):
    markup = ReplyKeyboardRemove()
    bot.send_chat_action(message.chat.id, "Typing")
    #Welcome Message
    bot.send_photo(message.chat.id, start_img, "<b>Bienvenido al Chatbot de la ESFOT - EPN</b>", parse_mode="html")
    bot.send_message(message.chat.id, "Hola, me llamo Esfotito 🦉 y seré tu asistente para conocer sobre los procesos académicos en la ESFOT.")
    time.sleep(3)
    bot.send_message(message.chat.id, "\nPara continuar, por favor selecciona los comandos en el botón [Menú] de tu barra de acciones o, el botón [/] en el mismo lugar.")

'''--------- Respondes to /Aulas ------------'''


'''--------- Respondes to /Matriculas ------------'''
@bot.message_handler(commands=["matriculas"])
def matriculas_msg(message):
    #Texet separator
    separator = bot.send_message(message.chat.id, "<i> [ --- Has seleccionado Matriculas --- ]</i>", parse_mode="html")
    time.sleep(3)
    bot.edit_message_text("*** *** *** *** ***", message.chat.id, separator.message_id)
    bot.send_message(message.chat.id, matricula_title, parse_mode="html")

    #Survery to access the information
    bot.send_message(message.chat.id, "\nAntes de continuar, por favor responde la siguiente pregunta, para poder acceder a la informacion deseas.\n")

    #Suvery buttons
    markup = ForceReply()
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Selecciona una opcion: ")
    markup.add("Nivelacion", "Pregrado")
    msg = bot.send_message(message.chat.id, "<i><b>¿Cuál es el nivel académico que vas a cursar 👇?</b></i>", parse_mode="html", reply_markup=markup)
    bot.register_next_step_handler(msg, level_select)

#Level Select options
def level_select(message):
    if message.text == "Nivelacion":
        print("Hola")
    if message.text == "Pregrado":
        print("Adios")
    else:
        bot.send_message(message.chat.id, advise_title + "\n\nLa opción no es válida, por favor reintente.", parse_mode="html")
        markup = ForceReply()
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Selecciona una opcion: ")
        markup.add("Nivelacion", "Pregrado")
        msg = bot.send_message(message.chat.id, "<i><b>¿Cuál es el nivel académico que vas a cursar 👇?</b></i>", parse_mode="html", reply_markup=markup)
        bot.register_next_step_handler(msg, level_select)
        

'''--------- Respondes to /Practicas ------------'''


'''--------- Respondes to /Vinculacion ------------'''


'''--------- Respondes to /Preguntas_frecuentes ------------'''


'''--------- Respondes to /Contactos ------------'''


'''--------- Respondes to /Regresar ------------'''
@bot.message_handler(commands=["regresar"])
def back_cmd(message):
    set_commands
    separator = bot.send_message(message.chat.id, "<i> [ --- Regresando al menu principal... --- ] </i>", parse_mode="html")
    time.sleep(5)
    bot.edit_message_text("*** *** *** *** ***", message.chat.id, separator.message_id)
    bot.send_message(message.chat.id, "Para continuar, por favor selecciona los comandos en el botón [Menú] de tu barra de acciones o, el botón [/] en el mismo lugar.")


'''--------- Responses to Text ----------'''
@bot.message_handler(content_types=["text"])
def text_msgs(message):
    if message.text.startswith("/"):
        bot.send_chat_action(message.chat.id, "Typing")
        bot.send_message(message.chat.id, "Comando no disponible ‼" + "\n Intenta nuevamente con tu mensaje, por favor 👀")
    else:
        bot.send_chat_action(message.chat.id, "Typing")
        edit_message = bot.send_message(message.chat.id, "Tienes muchas dudas y Esfotito te las solucionará 👋")
        time.sleep(60)
        bot.edit_message_text(message.chat.id, "Gracias por preguntarle a <i><u>Esfotito</u></i> 🦉", message.chat.id, edit_message.message_id, parse_mode="html")
#----------------------------------------------------------------------
#Get Messages Function (With pollying infinity)
def get_msgs():
    bot.infinity_polling()


#Define commads menu----------------------------------------------------
def set_commands():
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Inicializa el bot."),
        telebot.types.BotCommand("/aulas", "Conoce acerca de la ubicación de las aulas corespondientes a cada facultad."),
        telebot.types.BotCommand("/matriculas", "Obten información acerca del proceso de matrículas."),
        telebot.types.BotCommand("/practicas", "Obten información acerca del proceso de prácticas pre-profesionales y pasantías."),
        telebot.types.BotCommand("/vinculacion", "Obten información acerca del proceso de prácticas comuitarias o vinculación social."),
        telebot.types.BotCommand("/preguntas_frecuentes", "Conoce las preguntas preguntes de los estudiantes."),
        telebot.types.BotCommand("/contactos", "Conoce los medios de comunicación con ESFOT - EPN."),
        telebot.types.BotCommand("/regresar", "Regresar al menú previo."),
    ])


# Main Funciton with infinity polling
if __name__ == "__main__":

    #Define Commands menu
    set_commands
    #Main Polling Bucle
    print(" ********************** Iniciando el Bot *********************** ")
    hilo_bot = threading.Thread(name="hilo_bot", target=get_msgs)
    hilo_bot.start()
    print(" ********************** Cerrando el Bot ************************ ")