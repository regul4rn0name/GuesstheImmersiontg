import telebot

bot = telebot.TeleBot("6877931851:AAHIpMInvzR0dTDXhy2PCeucEFojw0PFc9c", parse_mode=None)  # Replace "YOUR_BOT_TOKEN" with your actual bot token

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_all_messages(message):
    # Process the received message
    if message.text.lower() == "да":
        image_url = "https://i.imgur.com/vQSkmHE.jpg"
        bot.send_photo(message.chat.id, image_url)
    elif message.text.lower() == "нет":
        bot.reply_to(message, "Пидора ответ")

bot.infinity_polling()

#6629652190:AAG6NENECmE_fWLMyYffR4sOuGoYbnPygiA

