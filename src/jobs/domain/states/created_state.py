from src.jobs.domain.states.base import JobState

class CreatedState(JobState):
    def start(self, job):
        from src.jobs.domain.states.running_state import RunningState
        job.state = RunningState()

    def complete(self, job):
        raise Exception("Cannot complete a created job")

    def fail(self, job):
        from src.jobs.domain.states.failed_state import FailedState
        job.state = FailedState()
