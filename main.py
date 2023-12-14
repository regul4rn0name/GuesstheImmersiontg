import get
import matchdecode
import itemsname
import game
import telebot
from itemsname import item_dnames, localnames, good
from telebot import types
from matchdecode import hero,specific_player_items,mid
from get import fetched_id
from match_ids_module import match_ids


bot = telebot.TeleBot("6871169504:AAFx2hMVgp9AL4ZN50G33UF_u40k7LoJnsY")



# Add a dictionary to store user states based on chat ID
user_states = {}

@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    user_states[chat_id] = {'state': 'start'}  # Initialize user state
    # Rest of your existing code...

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_all_messages(message):
    chat_id = message.chat.id

    # Retrieve user state
    if chat_id in user_states:
        user_state = user_states[chat_id]
    else:
        user_states[chat_id] = {'state': 'start'}  # Initialize state if not found
        user_state = user_states[chat_id]

    # Modify your logic based on user state...
    
    # Example:
    if user_state['state'] == 'start':
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
    bot.reply_to(message, "Чтобы сообщить об ощибке или предложить идею писать @eblo69")
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_all_messages(message):

    strgood = "".join(good)
    if message.text.lower() == strgood.lower():
        markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
        markup.add("/start")
        bot.reply_to(message, f"Правильно,загаданым героем был:{strgood}\nСсылка на матч: https://www.dotabuff.com/matches/{match_ids[mid[0]]}",reply_markup=markup)


    else:
        markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
        markup.add("/start")
        bot.reply_to(message, f"Неправильно,загаданым героем был:{strgood}\nСсылка на матч: https://www.dotabuff.com/matches/{match_ids[mid[0]]}",reply_markup=markup)



bot.infinity_polling()
