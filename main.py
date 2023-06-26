import asyncio
import os
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Установите свой ключ API GPT-3.5 Turbo
openai.api_key = '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'

# Создайте бота и диспетчер
bot = Bot(token='5871193378:AAG47T5rPWd5_Ptos6eLb-nVuq2zq6SuC7Q')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Функция для обработки входящих сообщений
@dp.message_handler()
async def handle_message(message: types.Message):
    user_message = message.text

    # Проверка на символы "+" и "-"
    if user_message.startswith('+') or user_message.startswith('-'):
        return

    # Используйте API GPT-3.5 Turbo для получения ответа на входящее сообщение
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_message,
        max_tokens=1500
    )

    # Получите ответ от GPT-3.5 Turbo
    reply = response.choices[0].text.strip()

    # Отправьте ответ пользователю
    await bot.send_message(chat_id=message.chat.id, text=reply)

async def on_startup(dp):
    await bot.send_message(chat_id='YOUR_CHAT_ID', text='Бот запущен')

async def on_shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()

def main():
    # Запуск бота
    loop = asyncio.get_event_loop()
    loop.create_task(on_startup(dp))
    loop.create_task(dp.start_polling())
    try:
        loop.run_forever()
    finally:
        loop.close()

if __name__ == '__main__':
    main()
