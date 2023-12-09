from aiogram import Bot, Dispatcher
from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message

import Token

BOT_TOKEN = Token.BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет\nМеня зовут Эхо-бот!\nНапиши мне что нибудь')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Я создан для того чтобы отвечать\n'
        'на твои сообщения твоими же сообщениями'
    )


@dp.message(Command(commands=['support']))
async def process_support_command(message: Message):
    await message.answer('Ссылка на подержку https://t.me/Pikowet')


@dp.message(Command(commands=['contacts']))
async def process_support_message(message: Message):
    await message.answer('Вот Другие контакты поддержкт\n*Ссылка на вк*\n*Ссылка на инсту*\n*Номер телефона в ватсап*')


@dp.message(F.video)
async def process_sendVideo_message(message: Message):
    await message.answer_video(message.video[0].file_id)


@dp.message(F.sticker)
async def process_sendSticker_message(message: Message):
    await message.answer_video(message.sticker.file_id)


@dp.message(F.animation)
async def process_GIF_message(message: Message):
    await message.answer_animation(message.animation.file_id)


@dp.message(F.voice)
async def process_senVoice_message(message: Message):
    await message.answer_voice(message.voice.file_id)

@dp.message(F.photo)
async def process_sendPhoto_message(message: Message):
    await message.answer_photo(message.photo[0].file_id)


@dp.message()
async def send_echo(message: Message):
    await message.replay(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)