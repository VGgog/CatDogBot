import picture as pic
import telebot
import random 
from telebot import types

bot = telebot.TeleBot('1902988440:AAH4YHkumzx1Nmhx4otQ720GAXAhKenFp0A')


@bot.message_handler(commands = ['start'])
def bot_say_hi(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	butten_one = types.KeyboardButton('😺 Хочу котика 😺')
	butten_two = types.KeyboardButton('🐶 Хочу собачку 🐶')
	butten_three = types.KeyboardButton('🤖 О боте 🤖')
	markup.add(butten_one, butten_two)
	markup.add(butten_three)
	bot.send_message(message.chat.id, "Приветствую вас, если вы перешли сюда, то думаю,\
что хотите получить уйму милоты.\nНу что-же, наслаждайтесь.", reply_markup=markup)


@bot.message_handler(content_types = ['text'])
def bot_send_photo(message):
	if message.text == '😺 Хочу котика 😺':
		bot.send_photo(message.chat.id, random.choice(pic.cat))
	elif message.text == '🐶 Хочу собачку 🐶':
		bot.send_photo(message.chat.id, random.choice(pic.dog))
	elif message.text == '🤖 О боте 🤖':
		bot.send_message(message.chat.id, 'Я бот, который преподносит в этот мир чуточку милоты.\n\
Вы можете выбрать, что конкретнее хотите увидеть, собачек или кошечек.\n\
Для этого есть 2 кнопочки, нажимая на которые, вы можете выбрать кого конкретнее хотите увидеть.\n\
Третья кнопочка вызывает меня(но думаю вы с этим разобрались).\n\
Я не умею читать, поэтому ваши сообщения я не понимаю.\n\
Удачного вам умиления')
	else:
		bot.send_message(message.chat.id, "Я не умею читать, поэтому прошу нажимайте на кнопки.\n\
Ну-ну, пожайлуста😢😢😢")


bot.polling()