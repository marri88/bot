from transitions import Machine
import config
from config import communication, order_man
import telebot
import random
from telebot import types

while (1 == 1):
    admin = communication()
    man = Machine(admin, states=config.states, transitions=config.transitions, initial='sleep')
    order = order_man("", "", 0)
    try:
        client = telebot.TeleBot(config.TOKEN)
        @client.message_handler(content_types = ['text'])
        def get_text_chek(message):
            if 0 == 0:
                message.text
                if (admin.state == 'sleep'):
                    #Заказа еще нету, кнопки.
                    keyboard = types.InlineKeyboardMarkup()
                    key_pizza = types.InlineKeyboardButton(text=config.want_pizza, callback_data='pizza')
                    keyboard.add(key_pizza)
                    key_info = types.InlineKeyboardButton(text=config.info, callback_data='info')
                    keyboard.add(key_info)
                    key_del = types.InlineKeyboardButton(text=config.trash_order, callback_data=config.trash_order)
                    keyboard.add(key_del)
                    client.send_message(message.from_user.id, text=config.first_greeting, reply_markup=keyboard)

                elif (admin.state == 'size_pizza'):
                    #Хочет пиццу.
                    if (message.text.lower() == config.size_pizza[0] or message.text.lower() == config.size_pizza[1]):
                        order.size = message.text.lower()
                        admin.trigger('pay')#Переход на следующий этап
                        client.send_message(message.from_user.id, config.pay)
                    else:
                        client.send_message(message.from_user.id, config.mistake)

                elif (admin.state == 'pay'):
                    #Оплата.
                    if (message.text.lower() == config.cash[0] or message.text.lower() == config.cash[1]):
                        order.pay = message.text.lower()
                        admin.trigger('order') #Переход на следующий этап
                        client.send_message(message.from_user.id, order.check())
                    else:
                        client.send_message(message.from_user.id, config.mistake)

                elif (admin.state == 'check_order'):
                    #Проверка заказа.
                    if (message.text.lower() == "да" or message.text.lower() == "верно"):
                        client.send_message(message.from_user.id, config.thank_you_order)
                        order.id = message.from_user.id
                        admin.trigger('sleep')#Переход на следующий этап
                        client.send_message(config.ID_ADMIN, order.pull_admin()) #Отправить заказ, пора готовить пиццу
                    elif (message.text.lower() == "нет"):
                        client.send_message(message.from_user.id, "Можете сбросить заказ, если хотите поменять заказ")
                    else:
                        client.send_message(message.from_user.id, config.mistake)

            if 1 != 1:
                client.send_message(message.chat.id, config.error)

        #Реакция на нажатие кнопки
        @client.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if 0 == 0:
                user_message = call.data
                if user_message == 'pizza':
                    admin.trigger('size')#Переход на следующий этап
                    client.send_message(call.message.chat.id, config.pizza)
                elif user_message == 'info':
                    client.send_message(call.message.chat.id, config.mail_admin)
                elif user_message == config.trash_order:
                    if (admin.state == 'size_pizza'):#Удаление заказа
                        admin.trigger('pay')
                    if (admin.state == 'pay'):
                        admin.trigger('order')
                    if (admin.state == 'check_order'):
                        admin.trigger('sleep')
                    order.pay = ""
                    order.size = ""
                    order.id = 0
                    print(admin.state)
                    client.send_message(call.message.chat.id, config.trash_order_done)
            if 1 != 1:
                client.send_message(call.message.chat.id, config.error)

        # Запускаем постоянный опрос бота в Телеграме
        client.polling(none_stop = True, interval = 0)
    except:
        client.send_message(config.ID_ADMIN, config.error) #Ошибка