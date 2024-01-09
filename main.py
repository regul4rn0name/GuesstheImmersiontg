import threading
import requests
import random
import telebot
from telebot import types
import mysql.connector


execution_lock = threading.Lock()

bot = telebot.TeleBot("6871169504:AAFx2hMVgp9AL4ZN50G33UF_u40k7LoJnsY")
match_ids = []
hero = []
specific_player_items = []
mid = []
item_dnames = []
localnames = []
good = []
fetched_id = []


last_message = {}

def get():
    item_dnames.clear()
    localnames.clear()
    hero.clear()
    mid.clear()
    specific_player_items.clear()
    match_ids.clear()


    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="matches",
        )

        mycursor = mydb.cursor()
        sql = "SELECT match_id FROM `Andrey`"
        mycursor.execute(sql)
        fetched_match_ids = mycursor.fetchall()

        
        match_ids.extend([match_id[0] for match_id in fetched_match_ids])
        fetched_id.extend([match_id[0] for match_id in fetched_match_ids])

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        mycursor.close()
        mydb.close()

def decode():
    print(len(match_ids))
    ranid = random.randint(0, len(match_ids) - 1)
    mid.append(ranid)
    print("aboba", mid)
    api_key = "your_api_key_here"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    try:
        url = f"https://api.opendota.com/api/matches/{match_ids[ranid]}"
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        match_details = response.json()

        if 'players' in match_details:
            for player in match_details['players']:
                if player.get('account_id') == 86853590:
                    hero.append(player[f"hero_id"])
                    items = []
                    for i in range(6):
                        item_key = f"item_{i}"
                        if item_key in player:
                            item_id = player[item_key]
                            items.append(item_id)
                            specific_player_items.append(item_id)

                    print(f"Items for Player with ID 86853590 in Match ID {match_ids[ranid]}: {items} On hero:{hero}")

            print(f"Successful response for Match ID {match_ids[ranid]}")
    except requests.exceptions.HTTPError as errh:
        if response.status_code == 500:
            print(f"Error 500: Internal Server Error for Match ID {match_ids[ranid]}")
        else:
            print(f"HTTP Error {response.status_code}: {errh}")

    print("Specific player (ID 86853590) item IDs:", specific_player_items)

def get_item_names():
    exclude = [115, 116, 117, 118, 130, 131, 132, 133, 134, 127, 124, 125, 122, 24]

    url = "https://raw.githubusercontent.com/odota/dotaconstants/master/build/item_ids.json"
    url2 = "https://raw.githubusercontent.com/odota/dotaconstants/master/build/items.json"
    url3 = "https://raw.githubusercontent.com/odota/dotaconstants/master/build/heroes.json"
    response2 = requests.get(url2)
    response = requests.get(url)
    response3 = requests.get(url3)

    if response.status_code == 200:
        item_data = response.json()
        dname_data = response2.json()
        heroname = response3.json()
        for x in range(0, 2):
            ranh = random.randint(1, 138)
            while ranh in hero or ranh in exclude:
                ranh = random.randint(1, 138)
            hero.append(ranh)

        item_names = []

        for item_id in specific_player_items:
            item_name = item_data.get(str(item_id), )
            item_names.append(item_name)

        for item_tag in item_names:
            item_dname = dname_data.get(str(item_tag), {}).get('dname', "None")
            item_dnames.append(item_dname)
        for heros in hero:
            localname = heroname.get(str(heros), {}).get('localized_name', "None")
            localnames.append(localname)
        good.clear()
        good.append(localnames[0])
        random.shuffle(localnames)
        print(item_dnames, localnames, good)
    else:
        print("Failed to fetch item data")
        return None

@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    last_message[chat_id] = message

    with execution_lock:
        get()
        decode()
        get_item_names()
        game()
        send(message)

def send(message):
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

def game():
    print(item_dnames, localnames)
    guess = good[0]
    if str(guess) == str(good[0]):
        print("You won!", good[0])
    else:
        print("You lost", good[0])

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "To report an error or suggest an idea, contact @eblo69")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_all_messages(message):
    chat_id = message.chat.id
    strgood=""
    strgood = "".join(good)
    good.clear()

    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add("/start")

    if message.text.lower() == strgood.lower():
        bot.reply_to(message, f"Correct! The hero was: {strgood}\nMatch link: https://www.dotabuff.com/matches/{match_ids[mid[0]]}", reply_markup=markup)
        
    else:
        bot.reply_to(message, f"Incorrect! The hero was: {strgood}\nMatch link: https://www.dotabuff.com/matches/{match_ids[mid[0]]}", reply_markup=markup)
        

bot.infinity_polling()
