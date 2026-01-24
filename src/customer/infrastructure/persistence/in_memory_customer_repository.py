"""Customer infrastructure: In-memory customer repository adapter."""
from typing import Dict, List, Optional
from uuid import UUID, uuid4
from domain.adapter import Adapter
from customer.domain.customer import Customer
from customer.domain.repositories import CustomerRepository


class InMemoryCustomerRepository(CustomerRepository, Adapter):
    """
    In-memory implementation of CustomerRepository.

    This is an Adapter in the Ports and Adapters architecture.
    """

    def __init__(self):
        self._customers: Dict[UUID, Customer] = {}

    def add(self, entity: Customer) -> None:
        """Add a new customer."""
        self._customers[entity.customer_id] = entity

    def get(self, entity_id: UUID) -> Optional[Customer]:
        """Get a customer by ID."""
        return self._customers.get(entity_id)

    def update(self, entity: Customer) -> None:
        """Update an existing customer."""
        if entity.customer_id in self._customers:
            self._customers[entity.customer_id] = entity

    def delete(self, entity_id: UUID) -> None:
        """Delete a customer by ID."""
        if entity_id in self._customers:
            del self._customers[entity_id]

    def find_all(self) -> List[Customer]:
        """Find all customers."""
        return list(self._customers.values())

    def find_by_email(self, email: str) -> Optional[Customer]:
        """Find a customer by email address."""
        for customer in self._customers.values():
            if customer.email.value == email:
                return customer
        return None

    def next_identity(self) -> UUID:
        """Generate next customer identity."""
        return uuid4()
