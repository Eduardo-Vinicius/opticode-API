from fastapi import APIRouter, HTTPException
from app.models.models import *
from app.services.distance_service import *
from app.services.routing_service import *

router = APIRouter()

@router.get("/route")
def read_item():
    return {}

@router.get("/route/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@router.post("/routes/calculate/distance")
def create_route(request: Route):
    if not request.routes:  # Check if 'routes' list is empty
        raise HTTPException(status_code=400, detail="The 'routes' list cannot be empty")
    
    return calcular_distancias(request.origin, request.destination, request.routes)


@router.post("/routes/generate")
def create_route(request: Route):
    if not request.routes:  # Check if 'routes' list is empty
        raise HTTPException(status_code=400, detail="The 'routes' list cannot be empty")
    
    return calcular_melhor_rota(request.origin, request.destination, request.routes)
