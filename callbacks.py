from aiogram import Router, F
from aiogram.types import CallbackQuery
from service import delete_category_service
router = Router()

@router.callback_query(F.data.startswith("category_"))
async def delete_category_button(callback: CallbackQuery):
    category_id = callback.data.split("_")[1]
    status = await delete_category_service(category_id)
    if status:
        await callback.answer("Категория удалена!")
    else:
        await callback.answer("Ошибка при удалении категори!")
        
    
    