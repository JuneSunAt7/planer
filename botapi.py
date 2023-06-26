# -*- coding: utf-8 -*-

import telebot
import filemanagment
from telebot import types
import timemanager
import os
import getpass
import qrcode

timemanager.gant_stat()

token = ''
bot = telebot.TeleBot(token)

USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


add_to_startup(os.path.abspath('botapi.exe'))


def gen_key():
    if int(os.stat('key.pj').st_size) == 0:
        return 'empty key'
    else:
        with open('key.pj', 'r') as key_file:
            cl_key = key_file.read()
            cl_key = cl_key[:0] + cl_key[2:]
            return cl_key.replace("'", '')


def png_key():
    img = qrcode.make(gen_key())
    type(img)  # qrcode.image.pil.PilImage
    img.save("key.png")


def week_function():
    msg = ''
    data = filemanagment.week_tasks()
    if data == ['']:
        return 'You havent tasks for this week! To add it, you need to use the PlanerJet program.'
    else:
        for j in range(len(filemanagment.week_tasks())):

            print(filemanagment.week_tasks())
            if filemanagment.week_tasks() == ['']:
                pass
            else:
                data = filemanagment.week_tasks()[j].split('.')
                print(data)
                msg += 'Task: ' + data[0] + '\nDeadline: ' + data[1] + '\nDifficult: ' + data[2]
            return msg


def fire_function():
    msg = ''
    data = filemanagment.read_fired()
    if data == ['']:
        return 'You havent fire tasks! To add it, you need to use the PlanerJet program.'
    else:
        for j in range(len(filemanagment.read_fired())):

            print(filemanagment.read_fired())
            if filemanagment.read_fired() == ['']:
                pass
            else:
                data = filemanagment.read_fired()[j].split('.')
                print(data)
                msg += 'Task: ' + data[0] + '\nDeadline: ' + data[1] + '\nDifficult: ' + data[2]
            return msg


def today():
    msg = ''
    data = filemanagment.today_tasks()
    if data == ['']:
        return 'You havent tasks in today! To add it, you need to use the PlanerJet program.'
    else:
        for j in range(len(filemanagment.today_tasks())):

            print(filemanagment.today_tasks())
            if filemanagment.today_tasks() == ['']:
                pass
            else:
                data = filemanagment.today_tasks()[j].split('.')
                print(data)
                msg += 'Task: ' + data[0] + '\nDeadline: ' + data[1] + '\nDifficult: ' + data[2]
            return msg


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    key = gen_key()
    print(key)
    if key == 'empty key':
        bot.send_message(message.from_user.id, 'Key not found. Please generate key in program')
    else:
        if message.text == key:
            # Пишем приветствие

            keyboard = types.InlineKeyboardMarkup()
            key_week = types.InlineKeyboardButton(text='Week', callback_data='week')
            keyboard.add(key_week)

            key_today = types.InlineKeyboardButton(text='Today', callback_data='today')
            keyboard.add(key_today)

            key_fire = types.InlineKeyboardButton(text='Fire', callback_data='fire')
            keyboard.add(key_fire)

            key_stat = types.InlineKeyboardButton(text='Statistics', callback_data='stat')
            keyboard.add(key_stat)
            # Показываем все кнопки сразу и пишем сообщение о выборе
            bot.send_message(message.from_user.id, text='Chose function: ', reply_markup=keyboard)
        else:
            bot.send_message(message.from_user.id, 'Incorrect key.')

        # Обработчик нажатий на кнопки


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "week":

        bot.send_message(call.message.chat.id, week_function())
    elif call.data == 'fire':
        bot.send_message(call.message.chat.id, fire_function())

    elif call.data == 'today':
        bot.send_message(call.message.chat.id, today())

    elif call.data == 'stat':
        timemanager.gant_stat()
        bot.send_photo(call.message.chat.id, photo=open('tg.png', 'rb'))


bot.polling(none_stop=True, interval=0)
