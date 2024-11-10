from kombu import Queue

URL_BASE = "http://appasp.sefaz.go.gov.br/Sintegra/Consulta/default.html"

class CeleryConfig:
    broker_url = "amqp://guest:guest@rabbitmq:5672//"
    result_backend = "redis://redis:6379/"
    imports = 'worker_scrape.tasks'

    task_queues = (
        Queue(name='web-scraping'),
    )
    task_routes = {
        'web-scraping': {'queue': 'web-scraping'},
    }
