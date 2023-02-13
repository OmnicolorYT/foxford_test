import telebot

token = "5803438952:AAF0yh7Tfn6golVVYdFUMUGa14Kshtmj5AQ"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Привет, я бот! Я умею искать информацию в интернете за тебя. Напиши свой запрос в сообщении ниже.")


@bot.message_handler()
def generate_request(message):
    msg = message.text
    msg_without_plus = msg.replace('+', '%2B')
    msg_without_spaces = msg_without_plus.replace(' ', '+')
    request = 'https://www.google.com/?q=' + msg_without_spaces
    bot.send_message(message.chat.id, request)


bot.infinity_polling()