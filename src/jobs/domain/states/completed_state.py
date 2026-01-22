from src.jobs.domain.states.base import JobState

class CompletedState(JobState):
    def start(self, job):
        raise Exception("Job already completed")

    def complete(self, job):
        raise Exception("Job already completed")

    def fail(self, job):
        raise Exception("Cannot fail a completed job")
