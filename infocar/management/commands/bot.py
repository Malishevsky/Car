
import telebot
from django.core.management import BaseCommand
from telebot import types

from infocar.models import Auto,Engine,Transmission

bot = telebot.TeleBot('5766269809:AAF6_O5BaU-KeFy6bTXHqPxlROTVRtEHnDY')

class Command(BaseCommand):
    def handle(self, *args, **options):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,f'Привет {message.from_user.first_name}')



@bot.message_handler(commands=['sort'])
def sort(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Двигатели',callback_data='Engine'))
    markup.add(types.InlineKeyboardButton('Коробки', callback_data='Transmission'))
    bot.send_message(message.chat.id,'Выберите сортировку',reply_markup=markup)



@bot.callback_query_handler(func=lambda call:True)
def call_back(call):
    char = ''

    if call.data == 'Engine':
        char = 'e'
        markup_engine = types.InlineKeyboardMarkup()
        for i in Engine.objects.all():
            markup_engine.add(types.InlineKeyboardButton(f'{i.name}', callback_data=f'engine{i.id}'))
        bot.send_message(call.message.chat.id, 'Выбери двигатель',reply_markup=markup_engine )

    elif call.data =='Transmission':
        char = 't'
        markup_trans = types.InlineKeyboardMarkup()
        for i in Transmission.objects.all():
            markup_trans.add(types.InlineKeyboardButton(f'{i.name}', callback_data=f'trans{i.id}'))
        bot.send_message(call.message.chat.id, 'Выбери двигатель', reply_markup=markup_trans)

    if 'engine' in call.data:
        eng = Engine.objects.get(pk=call.data[-1])
        car_eng = eng.auto_set.all()
        for i in car_eng:
            res = f'''Авто : {i.firm} {i.model}  Цвет : {i.color}
                      {i.engine} {i.volume}л. Коробка : {i.transmission}
                      Цена : {i.price} USD
                      
'''
            bot.send_message(call.message.chat.id, res)
    elif 'trans' in call.data:
        tra = Transmission.objects.get(pk=call.data[-1])
        car_tra = tra.auto_set.all()
        for i in car_tra:
            res = f'''Авто : {i.firm} {i.model}  
            Цвет : {i.color}
            {i.engine} {i.volume}л. 
            Коробка : {i.transmission}
            Цена : {i.price} USD
                      
'''
            bot.send_message(call.message.chat.id, res)


bot.infinity_polling()

