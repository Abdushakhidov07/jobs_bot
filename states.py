from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from service import *
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards import *
router = Router()


class CreateCategory(StatesGroup):
    get_name = State()
    
class UpdateCategory(StatesGroup):
    get_id = State()
    get_new_name = State()

@router.message(F.text == "➕ Добавить Категорию")
@router.message(Command("add_category"))
async def add_category(message: Message, state: FSMContext):
    await message.answer("Введите имя категори -->")
    await state.set_state(CreateCategory.get_name)
    
    
    

@router.message(CreateCategory.get_name)
async def state_name_add(message: Message, state: FSMContext):
    status = await save_category(message.text)
    await state.clear()
    if status:
        await message.answer("Категория создана!")
    else:
        await message.answer("Ошибка при создании категори!!")
        
    
    


@router.message(F.text == "Изменить категори")
@router.message(Command("update_category"))
async def update_category(message: Message, state: FSMContext):
    await message.answer("Введите id категори -->")
    await state.set_state(UpdateCategory.get_id)
    
    
    

@router.message(UpdateCategory.get_id)
async def state_id_category(message: Message, state: FSMContext):
    await state.update_data(category_id = message.text)
    await message.answer("Введите имя категори -->")
    await state.set_state(UpdateCategory.get_new_name)


@router.message(UpdateCategory.get_new_name)
async def state_name_category(message: Message, state: FSMContext):
    data = await state.get_data()

    status = await update_category_service(data["category_id"], message.text)
    if status:
        await message.answer("Категория изменена!")
    else:
        await message.answer("Ошибка при изменении!")

    await state.clear()






@router.message(F.text == "Удалить Категорию")
@router.message(Command("delete_category"))
async def delete_category(message: Message):
    await message.answer("Выбирите категорию для удаления", reply_markup= await category_name_button())
    
    




@router.message(F.text == "📋 Показать категори")
@router.message(Command("get_category"))
async def add_category(message: Message):
    category = await get_category()
    text = ""
    for i in category:
        text+=f"""
Category id: {i['cotegory_id']}
Category name: {i['cotegory_name']}\n
        """
    await message.answer(text)