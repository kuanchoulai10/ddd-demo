"""Customer domain event: CustomerEmailUpdatedEvent."""
from uuid import UUID
from domain.domain_event import DomainEvent


class CustomerEmailUpdatedEvent(DomainEvent):
    """Domain event raised when customer email is updated."""

    def __init__(self, customer_id: UUID, new_email: str):
        super().__init__()
        self.customer_id = customer_id
        self.new_email = new_email
