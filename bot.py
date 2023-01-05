import time
import logging

from aiogram import executor, Bot, Dispatcher, types

TOKEN = "5414606856:AAFpiT-Go7rgTJptOG-mAm4eEsDXbus3Tmw"
MSG = "I remind you, {}, to write your girlfriend"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.first_name
    print(f"{user_id} {user_full_name} {time.asctime()}")

    await message.reply(f"Hi {user_full_name}")

    for i in range(15):
        time.sleep(3)

        await bot.send_message(user_id, MSG.format(user_name))


if __name__ == "__main__":
    executor.start_polling(dp)