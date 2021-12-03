import telebot

bot = telebot.TeleBot('5060889649:AAGKK-5kXc9BQ7BUpt1MR4ABy23RxlTsytc')


@bot.message_handler(commands=['website'])
def open_website(message):
    bot.send_message(message.chat.id, "Отличный выбор просто нажмите на кнопку: <a href='https://web.it-college.ru/i21s597/project%20of%20history'>Сайт по исстории</a>", parse_mode='html')


@bot.message_handler(commands='start')
def start(message):
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')
    send_mess_1 = f"Вас приветствует бот по исстории."
    bot.send_message(message.chat.id, send_mess_1, parse_mode='html')
    send_mess_2 = f"В этом боте присутствует ссылка на командный проект по исстории."
    bot.send_message(message.chat.id, send_mess_2, parse_mode='html')


@bot.message_handler(commands='help')
def help_1(message=None):
    send_mes1 = f"У этого бота есть команды они выглядят следующим образом: "
    bot.send_message(message.chat.id, send_mes1, parse_mode='html')
    send_mes2 = f"/start - эта команда отвечает за начало работы бота "
    bot.send_message(message.chat.id, send_mes2, parse_mode='html')
    send_mes3 = f"/website - эта команда отвечает за ссылку на проект по исстории"
    bot.send_message(message.chat.id, send_mes3, parse_mode='html')


bot.polling(none_stop=True)