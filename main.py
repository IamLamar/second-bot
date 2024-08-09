import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

group = types.ReplyKeyboardMarkup(resize_keyboard=True)
group.row("Наши ученики")
group.row("О нас")


students = types.ReplyKeyboardMarkup(resize_keyboard=True)
students.row("Lamar","Annur","Shirin")
students.row("Вернуться в меню")

@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id,"Приветствуем вас",reply_markup= group)

@bot.message_handler(func=lambda message:True)
def second(message):
    if message.text == "Наши ученики":
        bot.send_message(message.chat.id,"Ламар, Аннур, Ширин",reply_markup=students)
    elif message.text == "Вернуться в меню":
        bot.send_message(message.chat.id,"Наше меню",reply_markup=group)
    elif message.text == "О нас":
        bot.send_message(message.chat.id,"Адрес Айтиси",reply_markup=students)
    elif message.text ==("Lamar"):
        bot.send_message(message.chat.id,"Ламару 21 лет",reply_markup=students)
    elif message.text ==("Annur"):
        bot.send_message(message.chat.id,"Аннуру 15 лет",reply_markup=students)
    elif message.text ==("Shirin"):
        bot.send_message(message.chat.id,"Ширин 19 лет",reply_markup=students)
