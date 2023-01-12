import telebot
from config import TOKEN, keys
from extensions import APIException, CryptoConverter
from info import starting, helping


bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=['start', 'help'])
def repeat(massage: telebot.types.Message):
    if massage.text.lower() == '/start':
        bot.reply_to(massage, f'Приветствую, {massage.chat.username}! \n{starting} \n{helping}')
    elif massage.text.lower() == '/help':
        bot.reply_to(massage, helping)

@bot.message_handler(commands=['values'])
def values(massage: telebot.types.Message):
    text = 'Доступные валюты:'
    count = 0
    for key in keys.keys():
        count += 1 
        text += f'\n{str(count)}'
        text = '. '.join((text, key,)).capitalize()
    bot.reply_to(massage, text)


@bot.message_handler(content_types=["text"])
def convert(massage: telebot.types.Message):
    try:
        values = massage.text.lower().split(' ')

        if len(massage.text.split(' ')) > 3:
            raise APIException('Слишком много параметров!')
        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(massage, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(massage, f'Не удалось обработать команду\n{e}')
    else:
        
        text = f'Актуальный курс валюты "{quote}" по отношению к "{base}" в количестве "{amount}" - {float(total_base)*float(amount)}'
    
        bot.send_message(massage.chat.id, text)



bot.polling(none_stop=True)
