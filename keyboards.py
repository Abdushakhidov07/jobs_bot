from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from service import get_category


def category_batton():
    keybor = ReplyKeyboardMarkup(
        keyboard= [
            [KeyboardButton(text="📋 Показать категори")],
            [KeyboardButton(text="➕ Добавить Категорию")],
            [KeyboardButton(text="Изменить категори")],
            [KeyboardButton(text="Удалить Категорию")],
            
        ], resize_keyboard=True   
    )
    return keybor





async def category_name_button():
    keyboards = []
    categoryes = await get_category()
    for category in categoryes:
        keyboards.append([InlineKeyboardButton(text=f"{category['cotegory_name']}", callback_data=f"category_{category['cotegory_id']}")])
    keybor = InlineKeyboardMarkup(inline_keyboard=keyboards)
    return keybor

