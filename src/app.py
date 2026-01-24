"""FastAPI application entry point."""
from fastapi import FastAPI
from customer.api import router as customer_router


def create_app() -> FastAPI:
    """Create and configure FastAPI application."""
    app = FastAPI(
        title="Customer Management API",
        description="Domain-Driven Design example with Customer management",
        version="1.0.0"
    )

    # Include routers
    app.include_router(customer_router)

    return app


app = create_app()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
