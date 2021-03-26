from GoogleNews import GoogleNews
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.types import ContentTypes
from aiogram.dispatcher.filters.state import StatesGroup, State 
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN

bot = Bot(token=TOKEN, parse_mode="HTML")

dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Привет! Введите ключевое слово для поиска новостей')



@dp.message_handler(content_types=ContentTypes.TEXT)
async def text_filter(message: types.Message):
    googlenews = GoogleNews(lang='ru')
    googlenews.search(str(message.text))
    result = googlenews.get_links()
    count = 0
    for i in result:
        await message.answer(i)
        if count == 4:
            break
        count += 1



async def on_startup(dp):
    pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)