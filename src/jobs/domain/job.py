from src.jobs.domain.states.base import JobState
from src.jobs.domain.states.created_state import CreatedState

class Job:
    def __init__(self):
        self.state: JobState = CreatedState()

    def start(self) -> None:
        self.state.start(self)

    def complete(self) -> None:
        self.state.complete(self)

    def fail(self) -> None:
        self.state.fail(self)
