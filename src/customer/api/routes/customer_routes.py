"""Customer API: Customer routes."""
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from customer.application.use_cases import CreateCustomer
from customer.application.dtos import CreateCustomerRequest, CustomerResponse
from customer.domain.repositories import CustomerRepository
from customer.api.dependencies import get_customer_repository


# Create router
router = APIRouter(prefix='/api/customers', tags=['customers'])


# Request/Response models (API layer only)
class CreateCustomerApiRequest(BaseModel):
    """API request model for creating a customer."""
    first_name: str
    last_name: str
    email: EmailStr


class CustomerApiResponse(BaseModel):
    """API response model for customer."""
    customer_id: str
    first_name: str
    last_name: str
    email: str


@router.post(
    '',
    response_model=CustomerApiResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new customer",
    description="Creates a new customer with the provided information"
)
def create_customer(
    request: CreateCustomerApiRequest,
    repository: CustomerRepository = Depends(get_customer_repository)
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
        use_case = CreateCustomer(repository)
        response: CustomerResponse = use_case.execute(create_request)

        # Convert Application DTO to API response
        return CustomerApiResponse(
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
