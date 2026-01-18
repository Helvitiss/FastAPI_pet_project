from fastapi import APIRouter



router = APIRouter(prefix='/menu', tags=['menu'])





@router.get('')
async def get_menu():
    """Возвращает json меню"""

    return {
        "categories": [],
        "products": []
    }
