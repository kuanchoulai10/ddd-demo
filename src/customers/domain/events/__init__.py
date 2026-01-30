"""Customer domain events."""
from .customer_created_event import CustomerCreatedEvent
from .customer_email_updated_event import CustomerEmailUpdatedEvent

__all__ = [
    'CustomerCreatedEvent',
    'CustomerEmailUpdatedEvent',
]
