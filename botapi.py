# -*- coding: utf-8 -*-

import telebot
import filemanagment

bot = telebot.TeleBot('')

from telebot import types

def week_function():
    data = filemanagment.week_tasks()
    if len(data) == 0:
        return 'You have no tasks for this week! To add it, you need to use the PlanerJet program.'
    else:
        return data
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
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
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "week":

        bot.send_message(call.message.chat.id, week_function())
    elif call.data == 'fire':
        bot.send_message(call.message.chat.id, 'fire')


bot.polling(none_stop=True, interval=0)