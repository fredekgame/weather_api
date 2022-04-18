import pyowm 
import telebot
import time
from pyowm.utils.config import get_default_config
#
botToken = ('5179292832:AAGHTaTb0dJQgaA33dPvfsoElzJthYu73hQ') 
bot = telebot.TeleBot(botToken)
owmToken = ('b0cc036c5e1d3c065d1218286e4b72cd') 
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('b0cc036c5e1d3c065d1218286e4b72cd', config_dict)
mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text.lower() == "weather":
        bot.send_message(message.from_user.id, "Здравствуйте. Вы можете узнать здесь погоду. Просто напишите название города." + "\n")
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
            answer = "В городе " + message.text.title() + " сейчас " + weather.detailed_status + "." + "\n"
            answer += "Температура около: " + str(temp) + " С" + "\n"
            answer += "Максимальная температура: " + str(temp_max) + " C" + "\n"
            answer += "Минимальная температура: " + str(temp_min) + " C" + "\n"
            answer += "Ветер: " + str(wind) + " m/c" + "\n"
            answer += "Дата: " + str(timer) + "\n\n"
            if temp < -10 and weather.detailed_status == "снег":
                answer += "Сегодня очено холодно, одеайтесь тепло!"
            elif temp < -10 and weather.detailed_status == "дождь":
                answer += "Сегодня дождь, хорошо одевайтесь." 
            elif temp < -10 and weather.detailed_status == "пасмурно":
                answer += "Сегодня прохладно, одевайтесь потеплее."
            elif temp < -10 and weather.detailed_status == "ясно":
                answer += "Сегодня солнышко, хорошо одевайтесь."
            elif temp < 0 and weather.detailed_status == "снег":
                answer += "Сегодня снег, одевайтесь тепло!" 
            elif temp < 0 and weather.detailed_status == "дождь":
                answer += "Сегодня дождь, хорошо одевайтесь."
            elif temp < 0 and weather.detailed_status == "пасмурно":
                answer += "Сегодня прохладно, одевайтесь потеплее."
            elif temp < 0 and weather.detailed_status == "ясно":
                answer += "Сегодня солнышко, хорошо одевайтесь." 
            elif temp < 10 and weather.detailed_status == "снег":
                answer += "Сегодня град, седите дома!"
            elif temp < 10 and weather.detailed_status == "дождь":
                answer += "Сегодня дождь, хорошо одевайтесь."
            elif temp < 10 and weather.detailed_status == "пасмурно":
                answer += "Сегодня прохладно, возьмите куртку."
            elif temp < 10 and weather.detailed_status == "ясно":
                answer += "Сегодня солнышко, выходитее гулять!"
            elif temp < 25 and weather.detailed_status == "снег":
                answer += "Сегодня град, седите дома!"
            elif temp < 25 and weather.detailed_status == "дождь":
                answer += "Сегодня дождь, возьмите курку."
            elif temp < 25 and weather.detailed_status == "пасмурно":
                answer += "Сегодня прохладно, куртка не помешает."
            elif temp < 25 and weather.detailed_status == "ясно":
                answer += "Сегодня солнышко, одевайтесь посвободней и выходитее гулять!"
            elif temp > 25 and weather.detailed_status == "снег":
                answer += "Сегодня град, седите дома!"
            elif temp > 25 and weather.detailed_status == "дождь":
                answer += "Сегодня дождь, возьмите курку."
            elif temp > 25 and weather.detailed_status == "пасмурно":
                answer += "Сегодня прохладно, кофта не помешает."
            elif temp > 25 and weather.detailed_status == "ясно":
                answer += "Сегодня очено жарко, отличный день чтобы покупаться!"
        except Exception:
            answer = "Город не найден, попробуйте снова.\n"
            print(time.ctime(), "User id:", message.from_user.id)
            print(time.ctime(), "Message:", message.text.title(), 'Error')
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)