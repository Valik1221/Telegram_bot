import telebot
from dotenv import load_dotenv
import os

# Завантаження змінних середовища з файлу .env
load_dotenv()

# Отримання токену бота з змінних середовища
bot_token = os.getenv("BOT_TOKEN")

# Ініціалізація бота
bot = telebot.TeleBot(token=bot_token)

# Словник з контактами лідерів
leaders_contacts = {
    "Христина": "+380978689038",
    "Людимила (Рекрутер)": "+380686192684",
    "Богдан (Лідер)": "+380971354618",
    "Ігор (Завгосп)": "+380982325135",
    "Дмитро (Пастор церкви)": "+380679476506",
    "Євгеній (Наставник)": "+380637010107"
}


@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Розклад")
    item2 = telebot.types.KeyboardButton("Сьогодні чергує")
    item3 = telebot.types.KeyboardButton("Список чергових")
    item4 = telebot.types.KeyboardButton("Контакти лідерів")
    markup.add(item1, item2, item3, item4)
    telegram_username = bot.get_me().username  # Отримання імені вашого бота з API Telegram
    bot.send_message(user.id, f"Привіт, {user.first_name}!\n"
                              f"Це lite-версія боту, тому сильно не бити :) \nЗ пропозиціями, скаргами, "
                              f"відгуками і т.д. звертайтеся в пп: https://t.me/{telegram_username}",
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Розклад")
def show_schedule(message):
    bot.send_message(message.chat.id, "Завтра у вас 19.09 (вівторок):\n"
                                      "8.00 - підйом\n"
                                      "8.20 - зарядка\n"
                                      "8.30 - сніданок\n"
                                      "10.00-11.30 - англійська, група Яни, у Zoom, онлайн заняття.\n"
                                      "12.00- історія для УСІХ, у Zoom, онлайн заняття \n"
                                      "https://us04web.zoom.us/j/5655004957?pwd=VHVnaS9yYnovaXE1azFTR3VNV3NKQT09\n"
                                      "13.00 - обід, важливо почати вчасно.\n"
                                      "13.30-15.00 - англійська, група Наталі у Google Meet,  онлайн заняття\n"
                                      "15.00 - 16.10 - настільні ігри з Женею для УСІХ\n"
                                      "16.30 - спорт, самостійно\n"
                                      "18.30 - вечеря, важливо почати вчасно\n"
                                      "19.00 - онлайн заняття з англійської з канадкою (для частини студентів).\n")


@bot.message_handler(func=lambda message: message.text == "Сьогодні чергує")
def show_next_in_line_today(message):
    bot.send_message(message.chat.id, "Луцик Антон :)")


@bot.message_handler(func=lambda message: message.text == "Список чергових")
def show_next_in_line_list(message):
    bot.send_message(message.chat.id, "1. Босий Артур (18 вересня)\n"
                                      "2. Луцик Антон (19 вересня)\n"
                                      "3. Волошин Павло (20 вересня)\n"
                                      "4. Войналович Олександр (21 вересня)\n"
                                      "5. Клобуцький Матвій (22 вересня)\n"
                                      "6. Кузьмич Валентин (23 вересня)\n"
                                      "7. Букша Антон (24 вересня)\n"
                                      "8. Левчук Артур (25 вересня)\n"
                                      "9. Мажинськас Олександр (26 вересня)\n"
                                      "10. Махов Антоній (27 вересня)\n"
                                      "11. Сиромятников Кирило (28 вересня)\n"
                                      "12. Сметаняк Денис (29 вересня)\n"
                                      "13. Щербаков Сергій (30 вересня)\n")


@bot.message_handler(func=lambda message: message.text == "Контакти лідерів")
def show_leaders_contacts(message):
    response = "Контакти лідерів:\n"
    for leader, contact in leaders_contacts.items():
        response += f"{leader}: {contact}\n"
    bot.send_message(message.chat.id, response)


# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
