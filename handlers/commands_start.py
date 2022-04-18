from aiogram import types
from misc import dp,bot
from .sqlit import reg_user
from .callbak_data import st
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

content_chat = -1001523112454
ids_user = []

markup = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='🔥Вперёд🔥', callback_data='go')
markup.add(bat_a)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    reg_user(message.chat.id)
    await bot.copy_message(chat_id=message.chat.id, from_chat_id= content_chat, message_id = 29, caption= """Салам алейкум ✊🏻

Так, я не любитель долго затягивать.

Вникаем в суть:
1 - Мы занимаемся арбитражном трафика.
2 - Работаем через тик ток
3 - Набираем команду 
4 - Зарабатываем с нуля от 400$

Если тебе интересно, зарабатывать с телефона, и постоянно расти в доходах, при этом уделять 2-3 часа в день.

То готов прям сегодня тебя научить и добавить в команду!

Газуем?""",reply_markup=markup)


