"""Customer application: Create Customer use case."""
from customers.domain.customer import Customer
from customers.domain.repositories import CustomerRepository
from customers.application.dtos import CreateCustomerRequest, CreateCustomerResponse


class CreateCustomerDomainService:
    """Use case for creating a new customer."""

    def __init__(self, customer_repository: CustomerRepository):
        """
        Initialize use case with dependencies.

        Args:
            customer_repository: Repository for customer persistence
        """
        self._customer_repository = customer_repository

    def execute(self, request: CreateCustomerRequest) -> CreateCustomerResponse:
        """
        Execute the create customer use case.

        Args:
            request: Create customer request data

        Returns:
            CustomerResponse: Created customer data

        Raises:
            ValueError: If customer with email already exists
        """
        # Check if customer already exists
        existing_customer = self._customer_repository.find_by_email(request.email)
        if existing_customer:
            raise ValueError(f"Customer with email {request.email} already exists")

        # Create new customer
        customer = Customer.create(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email
        )

        # Persist customer
        self._customer_repository.add(customer)

        # Return response
        return CreateCustomerResponse(
            customer_id=customer.customer_id,
            first_name=customer.name.first_name,
            last_name=customer.name.last_name,
            email=customer.email.value
        )
