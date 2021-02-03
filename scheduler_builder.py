from apscheduler.schedulers.background import BackgroundScheduler
import json
from datetime import datetime
from datetime import timedelta
from core_dealer import dealer


# build with file
def build(filename) -> BackgroundScheduler:
    scheduler = BackgroundScheduler()
    with open(filename) as fp:
        json_data = json.load(fp)
        for data in json_data:
            offset = int(data['offset'])
            status = data['status']
            scheduler.add_job(
                dealer,
                next_run_time=datetime.now() + timedelta(seconds=offset),
                kwargs=status)
    return scheduler
