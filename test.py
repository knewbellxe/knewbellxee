import telebot
import pyowm
import random





bot = telebot.TeleBot("1211323506:AAGhSe1jvLz9VlA19yUw9Xa_AeH_KVvd9mM")
owm = pyowm.OWM('e795f9cecf119755deb10f8f900c8c16' , language='ru')

#Функции

@bot.message_handler(content_types=['text'])


def get_weather(message):
    if message.text.lower() == "погода":
        bot.send_message(message.chat.id, "Какой город тебя интересует, бро?")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIMIF7hJ1G3UHhWxrpuv-iBWYp6Rq3CAAIJAAOvIM4Xo8rnln8cP9AaBA')
        bot.register_next_step_handler(message, get_city)
    else:
        bot.send_message(message.chat.id, "Бразель, напиши - погода")
        
@bot.message_handler(content_types=['text'])


def get_city(message):   

    observation = owm.weather_at_place( message.text )
    w = observation.get_weather()
    temp = w.get_temperature('celsius')['temp']
    wind = w.get_wind()['speed']
    pressure = w.get_pressure()['press']
    status = w.get_detailed_status()

    answer = "Тамурррррра! В городе " + message.text + " сейчас " + status + "." + "\n\n"
    answer += "А температура , ебать , ебать, около " + str(temp) + " C." + "\n\n"
    answer += "Атмосферное давление итить его - " + str(pressure) + " мм." + "\n\n"
    answer += "Скорость Авантюристического ветра, мать его! Приблизительно равна :  " + str(wind) + " м/с." + "\n\n"



    very_cold = ["Погода зимняя, тоска осенняя, желания летние." ,
             "Хочу лето, босоножки, футболку, солнце, море, волны..." ,
             "Выключите снег, включите солнце, разогрейте небо, налейте море и насажайте пальм." ,
             "Погода такая, что прогноз передают почти матом." ,
             "Хорошая погода.. если Вам такая нравится.."]
    cold = ["В отвратную погоду, в холодный дождь и снег - становятся приятней кофе, кот и плед." ,
        "Погода заставляет желать красненького... или черненького... Или средиземненького моря." ,
        "Черт, погода холоднее ведьминой сиськи! Надо бы согреться!" ,
        "Холод — самый назойливый компаньон из всех, кого я знаю." ,
        "Хороший полководец в такую погоду солдата под пули не выгонит."]
    cool = ["Судя по погоде, вместо ласточек прилетят пингвины." ,
        "Жалуетесь на погоду? Погоде следует либо радоваться, либо вообще ее не замечать, либо одно, либо другое." ,
        "Гидрометцентр — место, где ошибки погоду не делают." ,
        "Перемены погоды в течение одного дня плохо влияют на состояние как больных, так и здоровых." ,
        "Не бывает плохой погоды, бывает неподходящая одежда."]
    warm = ["А эта программка погоду показывает. Называется «Впадлу встать и в окно посмотреть»..." ,
        "... Не бывает плохой погоды, бывает плохое настроение." ,
        "Вы замечали, что у каждого месяца в году есть свой запах? Для меня лучше всего пахнут октябрь и май." ,
        "Погода располагала к любви, а на огороде старый хрен заигрывал с молодой картошкой." ,
        "Почему настроение женщины меняется быстрее, чем погода?"]
    hot = ["Когда на улице так ярко сияет солнце, в музей ходят одни идиоты." ,
       "Летом выход из комнаты с кондиционером на улицу — переход из «зоны комфорта» в «зону конфорки»." ,
       "Излучайте тепло, теплее будет и Вам самим" ,
       "Есть хорошая примета - если жарко, значит лето..." ,
       "Жара в России - градус окружающий среды смыкается с градусом водки."]
    very_hot = ["Лето! Я изжарен, как котлета." ,
            "Жара хороша, в особенности зимой; но на что она сдалась нам летом?" ,
            "Тишину нарушало только шкворчание — это солнце поджаривало небеса." ,
            "Судя по погоде, двери ада давно пора менять!" ,
            "Жара – это когда мозги плавятся, и утекают с работы раньше вас."]


    if temp < -10:
         answer += (random.choice(very_cold))
    elif temp < 0:
         answer += (random.choice(cold))
    elif temp < 10: 
         answer += (random.choice(cool))
    elif temp < 20:
         answer += (random.choice(warm))
    elif temp < 30:
         answer += (random.choice(hot))
    else:
         answer += (random.choice(very_hot))

    
    bot.send_message(message.chat.id , answer)
    bot.register_next_step_handler(message, get_text_messages)


@bot.message_handler(content_types=['text'])

def get_text_messages(message):  
    if message.text.lower() == "зуб привет":
        bot.send_message(message.chat.id, "Выручай! Можешь мне пару соток закинуть? Курить совсем нечего ;(")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIMGF7g3FN3W3EfrdEB_RtxgSvJdpQYAAIDAAOvIM4XBEX7jKON-CMaBA')
        bot.register_next_step_handler(message, start)
    else:
        bot.send_message(message.chat.id, "Уз юж пхфф ич кар ... Бля, походу тебе нужна помощь, напиши - зуб привет")
        bot.register_next_step_handler(message, get_text_messages)



def start(message):
    if message.text.lower() == "переведу":
        bot.send_message(message.chat.id, "Ну а че, может замутим  тогда что нибудь по шурику? ЧАРАМ БАРАМ!")
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.chat.id, "походу, ты не втыкаешь, Тома, используй - переведу")
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAIMIl7hJ1oIjpHOKlozzr9Mq9WqnuiHAAIBAAOvIM4Xqk1PgZi0JzUaBA')
        bot.register_next_step_handler(message, start)
        

def get_name(message):
    bot.send_message(message.chat.id, 'Как дела то, бро? Знаю часто вспоминаете обо мне...  ')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    bot.send_message(message.chat.id, 'Когда с тобой увидимся, чепушила, пивка хоть попьем? Скинь бабосики на карту КАЧКА тогда, а то киви так заблокировать могут, если счет высылать буду постоянно')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIMHl7hJsv9oR_2g8naEkE9fziOwBgQAAIHAAOvIM4X0RwdyYzX4CYaBA')



bot.polling(none_stop=True, interval=0)



