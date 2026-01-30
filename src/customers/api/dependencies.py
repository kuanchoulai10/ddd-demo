"""Customer API: Dependency injection providers."""
from typing import Generator
from fastapi import Depends
from customers.domain.repositories import CustomerRepository
from customers.infrastructure.persistence import InMemoryCustomerRepository
from customers.application.use_cases.create_customer import CreateCustomerDomainService


# Singleton instance (in real app, this could be a database connection pool)
_customer_repository_instance = InMemoryCustomerRepository()


def get_customer_repository() -> Generator[CustomerRepository, None, None]:
    """
    Dependency provider for CustomerRepository.

    This function can be easily replaced in tests or different environments.
    Returns the abstract interface, not the concrete implementation.

    Yields:
        CustomerRepository: Repository instance
    """
    yield _customer_repository_instance

def get_create_customer_use_case(
    repository: CustomerRepository = Depends(get_customer_repository)
) -> CreateCustomerDomainService:
    """
    Dependency provider for CreateCustomer use case.

    Args:
        repository: Injected CustomerRepository
    """
    return CreateCustomerDomainService(repository)