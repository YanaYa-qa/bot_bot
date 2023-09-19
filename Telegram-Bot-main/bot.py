#библиотеки, которые загружаем из вне
import telebot
TOKEN = '6353457290:AAFQWiUD793tDLH8-6iqHVPtZKqZ3thhw1A'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("💜 Мой гит")
	item2 = types.KeyboardButton("👾 Написать мне")
	item3 = types.KeyboardButton("🦄 Сайт-визитка")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Привет тебе, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '💜 Мой гит':
			bot.send_message(message.chat.id, 'https://github.com/YanaYa-qa')
		elif message.text == '👾 Написать мне':
			bot.send_message(message.chat.id, 'http://t.me/yanaya19')
		elif message.text == '🦄 Сайт-визитка':
		    bot.send_message(message.chat.id, 'https://yanaya-qa.github.io/')
		else:
			bot.send_message(message.chat.id, 'Что-то на непонятном 🙃')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
