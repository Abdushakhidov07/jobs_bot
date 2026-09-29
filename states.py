from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from service import *
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()


class CreateCategory(StatesGroup):
    get_name = State()


@router.message(F.text == "➕ Добавить Категорию")
@router.message(Command("add_category"))
async def add_category(message: Message, state: FSMContext):
    await message.answer("Введите имя категори -->")
    await state.set_state(CreateCategory.get_name)
    
    
    

@router.message(CreateCategory.get_name)
async def state_name_add(message: Message, state: FSMContext):
    status = await save_category(message.text)
    if status:
        await message.answer("Категория создана!")
    else:
        await message.answer("Ошибка при создании категори!!")
        
    
    
