from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_kb = InlineKeyboardMarkup(resize_keyboard=True)
inline_button1 = InlineKeyboardButton(text="Product1", callback_data='product_buying')
inline_button2 = InlineKeyboardButton(text="Product2", callback_data='product_buying')
inline_button3 = InlineKeyboardButton(text="Product3", callback_data='product_buying')
inline_button4 = InlineKeyboardButton(text="Product4", callback_data='product_buying')
inline_kb.row(inline_button1, inline_button2, inline_button3, inline_button4)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Рассчитать')
button3 = KeyboardButton(text='Купить')

kb.insert(button2)
kb.insert(button)
kb.add(button3)
