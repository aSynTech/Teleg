import asyncio

from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)

# API_link = "https://api.telegram.org/bot5398528747:AAFAP4-PSaQYIJ4vtBiXX6kuz8WMLXNJB0k"
# updates = requests.get(API_link + "/getUpdates?offset=-1").json()

# print(updates)

# message = updates["result"][0]["message"]
# chat_id = message["from"]["id"]
# text= message["text"]

# send_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text=Привет, ты написал {text}")
# print("helljklkjlo world", 1 + "1")
