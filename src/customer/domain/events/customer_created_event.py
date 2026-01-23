"""Customer domain event: CustomerCreatedEvent."""
from uuid import UUID
from domain.domain_event import DomainEvent


class CustomerCreatedEvent(DomainEvent):
    """Domain event raised when a customer is created."""

    def __init__(self, customer_id: UUID, email: str):
        super().__init__()
        self.customer_id = customer_id
        self.email = email
