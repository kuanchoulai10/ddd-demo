"""Customer API: Dependency injection providers."""
from typing import Generator
from customer.domain.repositories import CustomerRepository
from customer.infrastructure.persistence import InMemoryCustomerRepository


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
