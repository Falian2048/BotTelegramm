import telebot

bot = telebot.TeleBot("883670130:AAEbsDcZqWMYJgTKewb-qAmkDi_YCWs98Pg")


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет, если хочешь узнать ДЗ пропиши /dz")

@bot.message_handler(commands=['dz'])
def send_dz(message):
	dz1 = open('DZ.txt')
	dz = dz1.read()
	bot.send_message(message.chat.id, "Вот тебе и ДЗ")
	bot.send_message(message.chat.id, dz)
	dz1.close()
    #bot.forward_message(-1001433728771, 414567692, 29)


bot.polling( none_stop = True )
