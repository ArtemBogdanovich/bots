import telebot
from telebot import types
import time

bot = telebot.TeleBot("---")


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Получить файл")
    markup.row(btn1)
    bot.send_message(
        message.chat.id, "Привет! Ты хочешь получить файл?", reply_markup=markup
    )


@bot.message_handler(func=lambda message: message.text == "Получить файл")
def send_file(message):
    file_path = "./Ознакомительный вариант.pdf"
    with open(file_path, "rb") as file:
        bot.send_document(message.chat.id, file)
    bot.send_message(
        message.chat.id,
        "Вы получили файл? Да или Нет?",
        reply_markup=create_response_markup(),
    )


def create_response_markup():
    markup = types.ReplyKeyboardMarkup()
    markup.row(types.KeyboardButton("Да"), types.KeyboardButton("Нет"))
    return markup


@bot.message_handler(func=lambda message: message.text in ["Да", "Нет"])
def file_received_confirmation(message):
    if message.text == "Да":
        bot.send_message(
            message.chat.id,
            "Пожалуйста, откройте файл и ознакомьтесь с его содержанием *Через некоторое время бот задаст вопрос*!",
        )
    else:  # "Нет"
        bot.send_message(
            message.chat.id,
            "Мы вышлем специально для вас ссылку на файл: * * * * * * *",
        )

    time.sleep(5)
    bot.send_message(
        message.chat.id, "Вам понравился материал, представленный в документе?"
    )
    bot.send_message(
        message.chat.id, "Да или Нет?", reply_markup=create_enjoyment_response_markup()
    )


def create_enjoyment_response_markup():
    markup = types.ReplyKeyboardMarkup()
    markup.row(types.KeyboardButton("Да!"), types.KeyboardButton("Нет!"))
    return markup


@bot.message_handler(func=lambda message: message.text in ["Да!", "Нет!"])
def material_enjoyment_response(message):
    if message.text == "Да!":
        bot.send_message(
            message.chat.id,
            "Тогда мы предлагаем вам не только новую подборку материала, но даже и пробное занятие с преподавателем!",
        )
        bot.send_message(
            message.chat.id,
            "Хотели бы вы попробовать? Да или Нет?",
            reply_markup=create_try_markup(),
        )
    else:
        bot.send_message(message.chat.id, "Хорошо, дайте знать, если измените мнение!")


def create_try_markup():
    markup = types.ReplyKeyboardMarkup()
    markup.row(
        types.KeyboardButton("Хотел(а) бы попробовать!"), types.KeyboardButton("Нет!")
    )
    return markup


@bot.message_handler(
    func=lambda message: message.text in ["Хотел(а) бы попробовать!", "Нет!"]
)
def try_response(message):
    if message.text == "Хотел(а) бы попробовать!":
        file_path = "./Ознакомительный вариант.pdf"
        with open(file_path, "rb") as file:
            bot.send_document(message.chat.id, file)
        bot.send_message(
            message.chat.id,
            "Держите файл! Преподаватель скоро свяжется с вами! Нажмите кнопку, чтобы связаться с преподавателем! Хороших вам будней и занятий, дорогой гость!",
            reply_markup=markup1(),
        )
    else:
        bot.send_message(message.chat.id, "Ну как хотите! *бьет по лбу бутылкой!*")


def markup1():
    markup = types.ReplyKeyboardMarkup()
    markup.row(types.KeyboardButton("Ссылка на преподавателя"))
    markup.row(types.KeyboardButton("Ссылка на канал преподавателя"))
    return markup


@bot.message_handler(
    func=lambda message: message.text
    in ["Ссылка на преподавателя", "Ссылка на канал преподавателя"]
)
def try_response(message):
    if message.text == "Ссылка на преподавателя":
        bot.send_message(message.chat.id, "https://t.me/Nastushkkrr")
    elif message.text == "Ссылка на канал преподавателя":
        bot.send_message(message.chat.id, "https://t.me/anastasiasuhanovaeng")
        

bot.polling(none_stop=True)
