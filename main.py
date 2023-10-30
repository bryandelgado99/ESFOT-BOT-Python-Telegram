import telebot
import time
import emoji
import os
from config import *

#Commands List
commands = ["start", "matriculas", "praticas", "vinculacion", "preguntas_frecuentes", "comentarios", "contactos"]

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
matricula_title = '<b><u>🎫 Guía de Matriculación:</u></b>'
pasantias_title = '<b><u>🧑‍💼👨‍💼 Prácticas Pre-profesionales y Pasantías:</u></b>'

#Bot Instances and Connection with API
bot = telebot.TeleBot(Telegram_Token)

#Actions and Responses for Bot-----------------------------------------

'''--------- Responses to /Start CMD -----------'''
@bot.message_handler(commands)
def start_cmd(message):
    bot.send_chat_action(message.chat.id, "Typing")
    #Welcome Message
    bot.send_message(message.chat.id, "Hola, me llamo Esfotito 🦉 y seré tu asistente para conocer sobre los procesos académicos en la ESFOT.")
    bot.send_photo(message.chat.id, start_img, "<b>Bienvenido al Chatbot de la ESFOT - EPN</b>", parse_mode="html")

'''--------- Respondes to /Matriculas ------------'''

'''--------- Respondes to /Practicas ------------'''

'''--------- Respondes to /Vinculacion ------------'''

'''--------- Respondes to /Preguntas_frecuentes ------------'''

'''--------- Respondes to /Comentarios ------------'''

'''--------- Respondes to /Contactos ------------'''

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
        bot.edit_message_text("Gracias por preguntarle a <i><u>Esfotito</u></i> 🦉", message.chat.id, edit_message.message_id, parse_mode="html")
#----------------------------------------------------------------------

# Main Funciton with infinity polling
if __name__ == "__main__":
    print(" ********************** Iniciando el Bot *********************** ")
    bot.infinity_polling()
    print(" ********************** Cerrando el Bot ************************ ")