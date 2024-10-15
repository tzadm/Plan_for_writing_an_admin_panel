from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from crud_functions import *
from keyboards import *
from path import *

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    qwert = State()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in get_all_products():
        await message.answer(f'Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}')
        for q in pictures:
            if i[1] in q:
                await message.answer_photo(open(q, 'br'), reply_markup=kb)
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(' Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calorie_norm = (float(10) * float(data['weight']) + 6.25 * float(data['growth'])
                    - float(5) * float(data['age'])) + float(5)
    await message.answer(f'Ваша норма калорий: {calorie_norm}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.'
                         '\nДля подсчёта нормы калорий нажмите кнопку "Рассчитать"',
                         reply_markup=kb)


@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение')
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
