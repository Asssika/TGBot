import datetime
import telebot
from telebot import types
import time
bot = telebot.TeleBot('5205328480:AAHjgNzAuXC_DYfMQnr0bY2hpT1x_iyvkDY')
keyboard = types.InlineKeyboardMarkup()
now = datetime.datetime.now()
compare1 = now.replace(hour=17, minute=58).strftime("%H:%M")
now = now.strftime("%H:%M %d.%m.%Y")
tmrw = datetime.datetime.now() + datetime.timedelta(days=1)
tmrw = tmrw.strftime("%H:%M %d.%m.%Y")
name = ''
timereg = ''
@bot.message_handler(regexp='start')
def start(message):
    global name
    global timereg
    name = message.chat.first_name
    timereg = datetime.datetime.now()
    timereg = timereg.strftime("%H:%M %d.%m.%Y")
    if compare1 > now:
        name = message.chat.first_name
        bot.send_message(message.from_user.id, f"{name}, поздравляю! ДАЛЕЕ ТЕКСТ...сегодня {now[6:]} в 19:00")
        time.sleep(((17 * 60 + 58) - (int(timereg[:2]) * 60 + int(timereg[3:5])))*60)
        remindertoday(message)
        return timereg
    elif compare1 < now:
        name = message.chat.first_name
        bot.send_message(message.from_user.id, f"{name}, поздравляю! ДАЛЕЕ ТЕКСТ...завтра {tmrw[6:]} в 19:00")
        time.sleep(((10 - int(timereg[:2])) * 60 + 14400)*60)
        remindermorning(message)
    else:
        bot.send_message(message.from_user.id, 'Напиши start')

def remindertoday(msg):
    key_stream = types.InlineKeyboardButton(text='Смотреть эфир', url='https://www.lamoda.ru/p/rtlabd984101/accs-vogueeyewear-ochki-solntsezaschitnye/')
    keyboard.add(key_stream)
    bot.send_message(msg.from_user.id, f"Готовы?{name}, сокро начнем", reply_markup=keyboard)

def remindermorning(message):
    key_eyewear = types.InlineKeyboardButton(text='Смотреть эфир', url='https://www.lamoda.ru/p/rtlabd984101/accs-vogueeyewear-ochki-solntsezaschitnye/')
    keyboard.add(key_eyewear)
    bot.send_message(message.from_user.id, f"Готовы?{name}, сокро начнем", reply_markup=keyboard)
    time.sleep(32380)
    remindertomorrow(message)

def remindertomorrow(message):
    key_eyewear = types.InlineKeyboardButton(text='Смотреть эфир',url='https://www.lamoda.ru/p/rtlabd984101/accs-vogueeyewear-ochki-solntsezaschitnye/')
    keyboard.add(key_eyewear)
    bot.send_message(message.from_user.id, f"Готовы?{name}, сокро начнем", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)