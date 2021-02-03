from apscheduler.schedulers.background import BackgroundScheduler


# scheduler manager
class SchedulerComposer:

    def __init__(self) -> None:
        super().__init__()
        self._scheduler = {}

    def has(self, name):
        schedule: BackgroundScheduler = self._scheduler.get(name, None)
        if schedule is not None:
            return True
        else:
            return False

    def add(self, name, schedule: BackgroundScheduler):
        schedule: BackgroundScheduler = self._scheduler.get(name, None)
        if schedule is not None:
            self._scheduler[name] = schedule
        else:
            # fixme throw Err if add tow times?
            pass

    def pause(self, name):
        schedule: BackgroundScheduler = self._scheduler.get(name, None)
        if schedule is not None:
            schedule.pause()

    def resume(self, name):
        schedule: BackgroundScheduler = self._scheduler.get(name, None)
        if schedule is not None:
            schedule.resume()

    # todo clear Or others action
