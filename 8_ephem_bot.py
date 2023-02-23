"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem
import logging

import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

"""logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')"""
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def greet_user(update, context):
    logger.info('Вызван /start')
    update.message.reply_text('Привет, пользователь. Ты вызвал команду /start')


def talk_to_me(update, context):
    user_text = update.message.text
    logger.info(user_text)
    update.message.reply_text(user_text)

def planets(update, context):
    enter_text = update.message.text
    enter_text = enter_text.split()
    name_planet = enter_text[1]
    if name_planet == 'Mars':
        planet = ephem.Mars('2023/02/23')
    elif name_planet == 'Pluto':
        planet = ephem.Pluto('2023/02/23')
    else:
        update.message.reply_text('Я не знаю эту планету')
        return
    constel = ephem.constellation(planet)
    logger.info('Вызван /planet')
    update.message.reply_text(constel)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
