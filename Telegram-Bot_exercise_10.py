import telebot
from telebot import types

# Little telegram bot with pyTelegramBotAPI library.

# My bot name - https://t.me/PoitreqmTelegramBot / PoitreqmTelegramBot

# https://pypi.org/project/pyTelegramBotAPI/

# https://github.com/eternnoir/pyTelegramBotAPI

# If you want to get token - need to open your Telegram and wirte to BotFather. BotFather is the one bot to rule them all.
# Use it to create new bot accounts and manage your existing bots. 1 - /start 2 - /newbot - and add NAMe and USERNAME of new bot.
# After you will get a token. Token need to put in botTimeWeb = telebot.TeleBot('YOUR TOKEN')

# Go in map where you have your file Telegram-Bot.by and open Power Shell console(Rigth Mouse Click -> Console) and start code in console Power Shell python Telegram-Bot.py

botTimeWeb = telebot.TeleBot("") # key


@botTimeWeb.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text == "hi":
        botTimeWeb.send_message(message.from_user.id, "Hello. Write /start")
    elif message.text == "/start":
        first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, welcome. This is my little telegram bot on Python. Do you want to continue?"
        markup = types.InlineKeyboardMarkup()
        button_yes = types.InlineKeyboardButton(text="Yes ✌️", callback_data="yes")
        markup.add(button_yes)
        botTimeWeb.send_message(
            message.chat.id, first_mess, parse_mode="html", reply_markup=markup
        )
    else:
        botTimeWeb.send_message(
            message.from_user.id, "I dont undestand you, write /start."
        )


@botTimeWeb.message_handler(commands=["start", "help"])
@botTimeWeb.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        if function_call.data == "yes":
            second_mess = (
                "I have a LinkedIn and GitHub profile- where would you like to go?"
            )
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton(
                    "LinkedIn", url="https://www.linkedin.com/in/iz2804/"
                )
            )
            markup.add(
                types.InlineKeyboardButton("GitHub", url="https://github.com/Poitreqm/")
            )
            botTimeWeb.send_message(
                function_call.message.chat.id, second_mess, reply_markup=markup
            )
            botTimeWeb.answer_callback_query(function_call.id)


botTimeWeb.infinity_polling()
