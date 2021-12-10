import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Do Smth 1")
    item2 = types.KeyboardButton("Do Smth 2")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Welcome to the chat, {0.first_name}!\n I am - <b>{1.first_name}</b>, created to help you organize your day.".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def m_bot(message):
    # bot.send_message(message.chat.id, message.text)
    if message.chat.type == 'private':
        if message.text == "Do Smth 1":
            bot.send_message(message.chat.id, "I am done")
        elif message.text == "Do Smth 2":
            bot.send_message(message.chat.id, "How r u")
        else:
            bot.send_message(message.chat.id, "I do not knoww")


bot.polling(none_stop=True)
