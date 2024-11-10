from celery import Celery
from worker_scrape import config

celery = Celery(
    __name__
)

celery.config_from_object(config.CeleryConfig)