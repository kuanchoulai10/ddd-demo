from abc import ABC, abstractmethod
from enum import Enum

class JobStatus(str, Enum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class JobState(ABC):
    @abstractmethod
    def start(self, job):
        raise NotImplementedError

    @abstractmethod
    def complete(self, job):
        raise NotImplementedError

    @abstractmethod
    def fail(self, job):
        raise NotImplementedError

