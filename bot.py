import telebot
import random

# Твой токен от BotFather
TOKEN = '8633082500:AAGdzYAFv26Fok0JNzGSTqyaDwppugs9f_M'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в гараж! Отправь /drop, чтобы получить свой первый номер.")

@bot.message_handler(commands=['drop'])
def drop_plate(message):
    letters = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']
    # Простая генерация
    l1 = random.choice(letters)
    l2 = random.choice(letters)
    l3 = random.choice(letters)
    num = random.randint(1, 999)
    region = random.randint(1, 199)
    
    plate = f"{l1} {num:03d} {l2}{l3} | {region}"
    bot.reply_to(message, f"Тебе выпал номер: <b>{plate}</b>", parse_mode='HTML')

# Запускаем бота
bot.polling(none_stop=True)
