import telebot
from telebot import types  # Из телебота импорт types

bot = telebot.TeleBot('5456362138:AAEhtYXUrEjc7Acc_RBVo9d3RSbnCFNoC58')  # команда подключения к боту


@bot.message_handler(commands=['start'])
def star(message):
    mess = f'Это пробный бот, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# Реакция на фото
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Прикольное фото!')


@bot.message_handler(commands=['Vk'])
def vk(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Вот он", url="https://vk.com/atrushakin"))
    bot.send_message(message.chat.id, "Vk моего создателя", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['Вк'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Vk', url='https://vk.com'))
    bot.send_message(message.chat.id, 'Ваш Vk', reply_markup=markup)


# Весь обробатываемый текст
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == f'Привет':
        bot.send_message(message.chat.id, "Доброго вечера или утра.", parse_mode='html')
    elif message.text == "Какой у меня id?":
        bot.send_message(message.chat.id, f"Вот такой:{message.from_user.id}", parse_mode='html')
    elif message.text == "Какой мотор?":
        bot.send_message(message.chat.id, "Правильный ответ. Мощный!")
    elif message.text == "Иконка":
        photo = open('123.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'я спать хочу':
        bot.send_message(message.chat.id, 'я тоже')
    elif message.text == 'код':
        document = open('321.txt', 'rb')
        bot.send_document(message.chat.id, document)
    else:
        bot.send_message(message.chat.id, "Непонял🤨.", parse_mode='html')


bot.polling(none_stop=True)