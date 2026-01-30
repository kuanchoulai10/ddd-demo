from fastapi import APIRouter
from .v1 import router as v1

router = APIRouter(prefix='/api', tags=['api'])

router.include_router(v1)
