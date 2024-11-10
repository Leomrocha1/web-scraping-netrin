from celery import Celery
import config

celery = Celery(__name__)

celery.config_from_object({
    'broker_url': config.CELERY_BROKER_URL,
    'result_backend': config.CELERY_RESULT_BACKEND
})


def scraping_message(cnpj):
    """
    Task responsável por enviar o cnpj para a FILA de web scraping.
    """
    task = celery.signature(
        'web-scraping', 
        queue='web-scraping',
        args=(cnpj,)
    ).apply_async()

    return task.id
