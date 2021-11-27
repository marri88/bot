

"""START-----------------------------------WORDS-----------------------------------------------------------------------"""

first_greeting = "Здравствуйте, лучшая пицца у нас!\n Готовы сделать заказ?"
pizza = "Какую вы хотите пиццу?\n  Большую или маленькую?"
mistake = "Не понял вас, простите"
pay = "Как вы будете платить?\n Наличкой или картой"
thank_you_order = "Спасибо за заказ, мы уже готовим вам лучшую пиццу"

want_pizza = "Хочу заказать пиццу"
trash_order = "Сбросить заказ"
trash_order_done = "Готово, заказ сброшен"
info = "Узнать контакты"
error = "Что-то не так"
size_pizza = ["большую", "маленькую"]
cash = ["наличкой", "картой"]

"""END-----------------------------------WORDS-----------------------------------------------------------------------"""


"""START-----------------------------------PRIVAT-----------------------------------------------------------------------"""

TOKEN = ''
mail_admin = ""
ID_ADMIN = ''

"""END-----------------------------------PRIVAT-----------------------------------------------------------------------"""



states=['sleep', 'size_pizza', 'pay', 'check_order']

transitions = [
    { 'trigger': 'sleep', 'source': 'check_order', 'dest': 'sleep' },
    { 'trigger': 'size', 'source': 'sleep', 'dest': 'size_pizza' },
    { 'trigger': 'pay', 'source': 'size_pizza', 'dest': 'pay' },
    { 'trigger': 'order', 'source': 'pay', 'dest': 'check_order' }
]


class order_man():
    size = ""
    pay = ""
    id = 0
    def __init__(self, size, pay, id):
        self.size = size
        self.pay = pay
        self.id = id
    def check(self):
        return "Давайте проверим заказ\n"+ self.size + " пиццу, " + " оплата " + self.pay + "?"
    def pull_admin(self):
        return str(self.id) + "\n" + self.pay + "\n" + self.size


class communication(object):
    pass
