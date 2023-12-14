import telebot
import time
from telebot import types
from collections import deque
from get import fetched_id
from match_ids_module import match_ids
import matchdecode
import itemsname
import game

TOKEN = '6871169504:AAFx2hMVgp9AL4ZN50G33UF_u40k7LoJnsY'
bot = telebot.TeleBot(TOKEN)

item_dnames = deque()
localnames = deque()
good = deque()
hero = deque()
mid = deque()
specific_player_items = deque()
match_ids = deque()

message_queue = deque()

@bot.message_handler(commands=['start'])
def handle_start(message):
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
    send_messages_from_queue()

@bot.message_handler(commands=['help'])
def handle_help(message):
    send_messages_from_queue()
    bot.reply_to(message, "Чтобы сообщить об ошибке или предложить идею, писать @eblo69")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_all_messages(message):
    strgood = "".join(good)
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add("/start")

    if message.text.lower() == strgood.lower():
        bot.reply_to(message, f"Правильно, загаданным героем был: {strgood}\nСсылка на матч: https://www.dotabuff.com/matches/{match_ids[mid[0]]}", reply_markup=markup)
    else:
        bot.reply_to(message, f"Неправильно, загаданным героем был: {strgood}\nСсылка на матч: https://www.dotabuff.com/matches/{match_ids[mid[0]]}", reply_markup=markup)

    send_messages_from_queue()

def send_messages_from_queue():
    while message_queue:
        queued_message = message_queue.popleft()
        bot.send_message(queued_message.chat.id, "Hello! I am a bot, and I'm responding in order.")
        # Add any additional logic for processing queued messages here

# Polling loop
while True:
    try:
        bot.polling(none_stop=True, interval=0)
        time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
