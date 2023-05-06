import pyowm 
import telebot
import time
from pyowm.utils.config import get_default_config
#
botToken = ('bot_token') 
bot = telebot.TeleBot(botToken)
owmToken = ('api_token') 
config_dict = get_default_config()
config_dict['language'] = 'en'
owm = pyowm.OWM('api_token', config_dict)
mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text.lower() == "weather":
        bot.send_message(message.from_user.id, "Hello. You can check the weather here. Just write the name of the city:" + "\n")
    else:
        try:
            observation = mgr.weather_at_place(message.text)
            weather = observation.weather
            temp_max = weather.temperature("celsius")["temp_max"]
            temp_min = weather.temperature("celsius")["temp_min"]
            wind = weather.wind()["speed"]
            temp = weather.temperature("celsius")["temp"]
            timer = weather.reference_time('iso')
            print(time.ctime(), "User id:", message.from_user.id)
            print(time.ctime(), "Message:", message.text.title(), temp, "C", temp_max, "C", temp_min, "C", wind, "m/c", timer, weather.detailed_status)
            answer = "In the city " + message.text.title() + " now " + weather.detailed_status + "." + "\n"
            answer += "Temperature around: " + str(temp) + " С" + "\n"
            answer += "Maximum temperature: " + str(temp_max) + " C" + "\n"
            answer += "Minimum temperature: " + str(temp_min) + " C" + "\n"
            answer += "Wind: " + str(wind) + " m/c" + "\n"
            answer += "Date: " + str(timer) + "\n\n"
            if temp < -10 and weather.detailed_status == "Snow":
                answer += "It's very cold today, dress warmly!"
            elif temp < -10 and weather.detailed_status == "Rain":
                answer += "It's raining today, dress well." 
            elif temp < -10 and weather.detailed_status == "Mainly cloudy":
                answer += "It's cold today, dress warmly."
            elif temp < -10 and weather.detailed_status == "It's clear":
                answer += "It's sunny today, dress well."
            elif temp < 0 and weather.detailed_status == "Snow":
                answer += "It's snowing today, dress warmly!" 
            elif temp < 0 and weather.detailed_status == "Rain":
                answer += "It's raining today, dress well."
            elif temp < 0 and weather.detailed_status == "Mainly cloudy":
                answer += "It's cold today, dress warmly."
            elif temp < 0 and weather.detailed_status == "It's clear":
                answer += "It's sunny today, dress well." 
            elif temp < 10 and weather.detailed_status == "Snow":
                answer += "Today hail, stay at home!"
            elif temp < 10 and weather.detailed_status == "дождь":
                answer += "It's raining today, dress well."
            elif temp < 10 and weather.detailed_status == "Mainly cloudy":
                answer += "It's cold today, bring a jacket."
            elif temp < 10 and weather.detailed_status == "It's clear":
                answer += "The sun is out today, go for a walk!"
            elif temp < 25 and weather.detailed_status == "Snow":
                answer += "Today hail, stay at home!"
            elif temp < 25 and weather.detailed_status == "Rain":
                answer += "It's raining today, grab a trigger."
            elif temp < 25 and weather.detailed_status == "Mainly cloudy":
                answer += "It's cold today, a jacket would be nice."
            elif temp < 25 and weather.detailed_status == "It's clear":
                answer += "Today is the sun, dress loose and go out for a walk!"
            elif temp > 25 and weather.detailed_status == "Snow":
                answer += "Today hail, stay at home!"
            elif temp > 25 and weather.detailed_status == "Rain":
                answer += "It's raining today, grab a trigger."
            elif temp > 25 and weather.detailed_status == "Mainly cloudy":
                answer += "It's chilly today, a jacket will not hurt."
            elif temp > 25 and weather.detailed_status == "It's clear":
                answer += "Today is very hot, great day to swim!"
        except Exception:
            answer = "City not found, please try again.\n"
            print(time.ctime(), "User id:", message.from_user.id)
            print(time.ctime(), "Message:", message.text.title(), 'Error')
        bot.send_message(message.chat.id, answer)
        
bot.polling(none_stop=True)
