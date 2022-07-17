import logging
from aiogram import Bot, Dispatcher, executor, types, exceptions
from sys import exit
import time
from config1 import *
from Mixinnn import new

bot_token = f"{Token1}"
if not bot_token:
    exit("Error: no token provided")
bot = Bot(token=bot_token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

dp.errors_handler(exception=exceptions.RetryAfter)
async def exception_handler(update: types.Update, exception: exceptions.RetryAfter):
    # Do something
    return True

@dp.message_handler(text='Код15')
async def cmd_test2(message: types.Message):
    await message.answer("Кто Бацьку не уважет, того бацька нагибает!!!")
    time.sleep(10)
    s1 = 0
    for i in range(100000):
        try:
            await bot.send_photo(chat_id=message.chat.id, photo=next(new))
            time.sleep(2)
            s1 += 1
            print(next(new), s1)
        except:
            time.sleep(0.1)
            print(f"time.sleep")
if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp)