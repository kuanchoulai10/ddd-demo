"""Customer API: Customer routes."""
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from customers.application.use_cases import CreateCustomerDomainService
from customers.application.dtos import CreateCustomerRequest, CreateCustomerResponse
from customers.api.dependencies import get_create_customer_use_case


# Request/Response models (API layer only)
class CreateCustomerApiRequest(BaseModel):
    """API request model for creating a customer."""
    first_name: str
    last_name: str
    email: EmailStr


class CreateCustomerApiResponse(BaseModel):
    """API response model for customer."""
    customer_id: str
    first_name: str
    last_name: str
    email: str

# Create router
router = APIRouter()

@router.post(
    '/',
    response_model=CreateCustomerApiResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new customer",
    description="Creates a new customer with the provided information"
)
def create_customer(
    request: CreateCustomerApiRequest,
    use_case: CreateCustomerDomainService = Depends(get_create_customer_use_case)
):
    """
    Create a new customer.

    - **first_name**: Customer's first name
    - **last_name**: Customer's last name
    - **email**: Customer's email address
    """
    try:
        # Convert API request to Application DTO
        create_request = CreateCustomerRequest(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email
        )

        # Execute use case with injected repository
        response: CreateCustomerResponse = use_case.execute(create_request)

        # Convert Application DTO to API response
        return CreateCustomerApiResponse(
            customer_id=str(response.customer_id),
            first_name=response.first_name,
            last_name=response.last_name,
            email=response.email
        )

    except ValueError as e:
        # Business rule violation or duplicate email
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )