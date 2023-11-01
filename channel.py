from config import *
import telebot
import threading
import time

#Bot Instance Connection to Telegram API
bot = telebot.TeleBot(Telegram_Token)

#Links and important data
calendario_2023b = '<a href="https://esfot.epn.edu.ec/index.php/esfot/676-calendario-academico-2023-b">Calendario Académico 2023-B</a>' + '\n'
guia_2023b = '<a href="https://esfot.epn.edu.ec/index.php/guia-del-estudiante">Guia del Estudiante 2023-B</a>' + '\n'
mapa_epn = '<a href="https://www.epn.edu.ec/institucion/ubicacion-geografica/">Mapa de la EPN</a>' + '\n'

#Media
start_img = open("./images/logo2.png", "rb")
add_circus = open("./channel_assets/images/mundo_circo.jpg", "rb")
epn_map = open("./channel_assets/images/mapa_epn.jpg", "rb")

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


#-------------------- Telegram Channel Bot News Deployment ---------------------
#Define a Welcome message
bot.send_message(Channel_ID, "Bienvenidos al Canal de <b><i>ESFOT NEWS</i></b>.", parse_mode="html")
bot.send_photo(Channel_ID, start_img, "Este canal tiene la funcion de mantener, a los integrantes, al tanto de las novedades en la ESFOT y le EPN.")
bot.send_message(Channel_ID, "<b>🤓 Bienvenidos y bienvenidas estudiantes, al periodo académico 2023-B 🦉 </b>\n", parse_mode="html")

bot.send_message(Channel_ID, "<b>Mapa Informativo del Campus de la EPN</b>", parse_mode="html")
bot.send_photo(Channel_ID, epn_map, "\n Estimados estudiantes, se les presenta el mapa del campus, con el cual podrán ubicarse en las distintas áreas que componen a la Escuela Politénica Nacional.")
bot.send_message(Channel_ID, "\n O, a su vez, pueden acceder al siguiente enlace, para conocer el mapa: " + mapa_epn, parse_mode="html")



#--------------------------------------------------------------------------------

#Get Messages Function (With pollying infinity)
def get_msgs():
    bot.infinity_polling()

# Main Funciton
if __name__ == "__main__":
    print(" ********************** Iniciando Canal *********************** ")
    hilo_bot = threading.Thread(name="hilo_bot", target=get_msgs)
    hilo_bot.start()
    print(" ********************** Cerrando Canal ************************ ")