from ast import main
import telebot
import requests as rs
from telebot import types
from .search import search_city

bot = telebot.TeleBot('5434924460:AAFszfluOZAAspa-4fcC_-Vwgb3AcAI0K6w')
API_KEY = '407fb8f6663cfd63b826d070e32a6f69'

@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(message.chat.id, 'Введите свой город', parse_mode='html')
    @bot.message_handler()
    def get_user_text(message):
        geoloc = search_city(message.text)        
        lat = geoloc[0]
        lon = geoloc[-1]
        CURRENT_WEATHER_API_CALL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
        auth = rs.post(CURRENT_WEATHER_API_CALL)
        res =  auth.json()     
        mess = f'Погода в твоем городе {res["main"]["temp_max"]}'
        bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup()
    website = types.KeyboardButton('\website')
    start = types.KeyboardButton('\start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Нажмите нужную вам кнопку', reply_markup=markup)


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить мой сайт,', url='http://noop696.pythonanywhere.com'))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)



bot.polling(non_stop=True)