import get
import matchdecode
import itemsname
import game
import telebot
from itemsname import item_dnames, localnames, good
from telebot import types
from matchdecode import hero, specific_player_items, mid
from get import fetched_id
from match_ids_module import match_ids

bot = telebot.TeleBot("6871169504:AAFx2hMVgp9AL4ZN50G33UF_u40k7LoJnsY")  # Замените 'YOUR_BOT_TOKEN' на токен вашего бота

# Словарь для хранения данных о последнем сообщении каждого пользователя
last_message = {}

@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    last_message[chat_id] = message  # Сохраняем последнее сообщение для пользователя

    item_dnames.clear()
    localnames.clear()
    good.clear()
    hero.clear()
    mid.clear()
    specific_player_items.clear()
    fetched_id.clear()
    match_ids.clear()
    get.main()
    matchdecode.main()
    itemsname.main()
    game.main()
    send()




def send():
    while "None" in item_dnames:
        item_dnames.remove("None")
    stritems = ",".join(item_dnames)
    strhero = ",".join(localnames)
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    but1 = types.KeyboardButton(localnames[0])
    but2 = types.KeyboardButton(localnames[1])
    but3 = types.KeyboardButton(localnames[2])
    markup.add(but1, but2, but3)
    bot.reply_to(message, stritems, reply_markup=markup)

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "Чтобы сообщить об ошибке или предложить идею писать @eblo69")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_all_messages(message):
    chat_id = message.chat.id
    strgood = "".join(good)

    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add("/start")

    if message.text.lower() == strgood.lower():
        bot.reply_to(message, f"Правильно, загаданным героем был: {strgood}\nСсылка на матч: https://www.dotabuff.com/matches/{match_ids[mid[0]]}", reply_markup=markup)
    else:
        bot.reply_to(message, f"Неправильно, загаданным героем был: {strgood}\nСсылка на матч: https://www.dotabuff.com/matches/{match_ids[mid[0]]}", reply_markup=markup)

bot.infinity_polling()


