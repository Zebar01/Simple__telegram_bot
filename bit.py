# This example show how to use inline keyboards and process button presses
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TELEGRAM_TOKEN = 'you_token'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# This example show how to use inline keyboards and process button presses
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TELEGRAM_TOKEN = 'you_token'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Остаться", callback_data=f"0002"),
                               InlineKeyboardButton("Пойти", callback_data=f"0003"))
    return markup

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    if message.text=='start':
        txt1="    start"
        ChatID=message.chat.id
        print(ChatID)
        bot.send_message(ChatID,txt1, reply_markup=gen_markup())        

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    print(call)
    if call.data == "0002":
        txt1="    Вы устраиваетесь поудобнее и ****"
        txt2="    text"
        #bot.send_photo(call.message.chat.id,'https://****.jpg')
        bot.send_message(call.message.chat.id,txt1)
        bot.send_message(call.message.chat.id,txt2, reply_markup=gen_markup())
    elif call.data == "0003":
        txt1="    гудбай"
        bot.send_message(call.message.chat.id,txt1)

bot.polling(none_stop=True)

