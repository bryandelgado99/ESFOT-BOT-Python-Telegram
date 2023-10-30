import telebot
import os

#Telegram API key
TOKEN = '6929440962:AAF8LpF4-d0HzVioDz2EReKSqMq1bmVzJHA'

#Bot Connection
bot = telebot.TeleBot(TOKEN)

#Bot Message List Commands
@bot.message_handler(commands=["start", "matriculas", "help"])

#Messages List Handler
def start_msg(message):
    bot.reply_to(message, 'Hola, me llamo Esfotito y seré tu asistente para conocer sobre los procesos académicos en la ESFOT.')
    
def matriculas_msg(message):
    bot.reply_to(message, 'Las matriculas del periodo 2023-B ya han empezado. No te quedes sin tu cupo.')
    
#Bot Reponses for "no commands" lines
@bot.message_handler(content_types=["text"])
def text_msgs(message):
    bot.send_message(message.chat.id, "Un momento, te dirijo con Esfotito")
        
#Bot Main Statement
if __name__ == '__main__':
    print("Iniciando el Bot")
    bot.infinity_polling()
    print("Fin del Bot")