import logging
from aiogram import Bot, Dispatcher, executor, types, exceptions
from sys import exit
import time
from config1 import *
from Mixinnn import new

bot_token2 = f"{Token8}"
print(bot_token2)
if not bot_token2:
    exit("Error: no token provided")
bot2 = Bot(token=bot_token2)
dp2 = Dispatcher(bot2)
logging.basicConfig(level=logging.INFO)

dp2.errors_handler(exception=exceptions.RetryAfter)
async def exception_handler(update: types.Update, exception: exceptions.RetryAfter):
    # Do something
    return True

@dp2.message_handler(text='Код15')
async def cmd_test2(message: types.Message):
    await message.answer("Кабан в строю!!!")
    time.sleep(10)
    s1 = 0
    for i in range(100000):
        try:
            await bot2.send_photo(chat_id=message.chat.id, photo=next(new))
            time.sleep(2)
            s1 += 1
            print(next(new), s1)
        except:
            time.sleep(0.1)
            print(f"time.sleep")

executor.start_polling(dp2)
#токен