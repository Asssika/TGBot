import time

import telebot
from telebot import types
bot = telebot.TeleBot('5205328480:AAHjgNzAuXC_DYfMQnr0bY2hpT1x_iyvkDY')

name = ''
surname = ''
target = ''
age = 0
@bot.message_handler(content_types=['text', 'document', 'audio'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "{0.first_name} Как тебя зовут?".format(message.from_user))
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    try:
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, 'Введите возраст цифрами, пожалуйста ')
            bot.register_next_step_handler(msg, get_age)
            return
        else:
            keyboard = types.InlineKeyboardMarkup()
            key_yes = types.InlineKeyboardButton(text='Поболтать', callback_data='yes')
            keyboard.add(key_yes)
            key_no = types.InlineKeyboardButton(text='Мне кое-что надо', callback_data='no')
            keyboard.add(key_no)
            key_eyewear = types.InlineKeyboardButton(text='Хочу очки', url='https://www.lamoda.ru/p/rtlabd984101/accs-vogueeyewear-ochki-solntsezaschitnye/')
            keyboard.add(key_eyewear)
            question = f'{name}, are you wanna talk or something another?'
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    except Exception as e:
        bot.reply_to(message, 'oooops')

# def get_data(message):
#     bot.send_message(message.from_user.id, f'{age}, ты хочешь просто поболтать или что-то конкретное?')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Lets talk');
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'What exactly?');
bot.polling(none_stop=True, interval=0)