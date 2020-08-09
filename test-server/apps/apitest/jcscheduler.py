from apscheduler.schedulers.background import BackgroundScheduler
from .view_extension import run_case
import json
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='scheduler_log.txt',
                    filemode='a')

_scheduler = BackgroundScheduler()

def _task_id(task):
    return "scheduler_%s"%task.id

def add_task(task,request):
    trigger_kwargs = json.loads(task.expr)
    _scheduler.add_job(run_case,args=[task.id,request],trigger="cron",id=_task_id(task),**trigger_kwargs)

def remove_task(task):
    job = _scheduler.get_job(_task_id(task))
    if job:
        _scheduler.remove_job(_task_id(task))

_scheduler._logger = logging

_scheduler.start()