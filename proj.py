# coding=windows-1251
import gptmessage
import telebot
from telebot import types
token='6801018540:AAE7owcsi2zZTVG-J1qmuVgiGs9soOVQf54'
bot=telebot.TeleBot(token, parse_mode='MARKDOWN')

print(gptmessage.get_responce('hello'))

@bot.message_handler(content_types='text')
def message_reply(message):
    user_id = message.chat.id
    text = message.text
    send_text_message(user_id, text)
    

def send_text_message(user_id, text):
    try:
        message = gptmessage.get_responce(text)
    except:
        message = 'Попробуйте еще раз'
    if message is None or len(message) < 1:
        message = 'Попробуйте еще раз'
    if len(message) >= 500:
        message = message[:500]
    try: 
        bot.send_message(user_id, message)
    except:
        bot.send_message(user_id, 'Попробуйте еще раз')
bot.infinity_polling()