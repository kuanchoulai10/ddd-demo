from fastapi import APIRouter
from .post_create_customer import router as create_customer_router

router = APIRouter(prefix='/customers', tags=['customers'])

router.include_router(create_customer_router)
