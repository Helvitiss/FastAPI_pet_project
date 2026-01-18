from fastapi import APIRouter

from backend.app.schemas.order import OrderResponse

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: int):
    return {
        "order_id": order_id,
        "status": "new"
            }



