from typing import Annotated

from fastapi import APIRouter, Path

router = APIRouter(prefix="/attractions", tags=["attractions"])


@router.get("/")
def get_list_attractions():
    return [
        "Moscow",
        "Piter",
        "Essentuki",
    ]


@router.get("/{attractions_id}/")
def get_attractions_by_id(attractions_id: Annotated[int, Path(ge=1, lt=500_000)]):
    return {
        "item": {
            "id": attractions_id,
        }
    }
