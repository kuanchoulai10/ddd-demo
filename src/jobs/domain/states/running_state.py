from src.jobs.domain.states.base import JobState

class RunningState(JobState):
    def start(self, job):
        raise Exception("Job already running")

    def complete(self, job):
        from src.jobs.domain.states.completed_state import CompletedState
        job.state = CompletedState()

    def fail(self, job):
        from src.jobs.domain.states.failed_state import FailedState
        job.state = FailedState()
