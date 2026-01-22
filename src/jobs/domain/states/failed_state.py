from src.jobs.domain.states.base import JobState

class FailedState(JobState):
    def start(self, job):
        raise Exception("Cannot start a failed job")

    def complete(self, job):
        raise Exception("Cannot complete a failed job")

    def fail(self, job):
        raise Exception("Job already failed")
