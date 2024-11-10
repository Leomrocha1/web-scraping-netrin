
from fastapi import APIRouter
from api.schemas.scrape import ScrapeSchema
from api.tasks import scraping_message, celery

router = APIRouter()

@router.post("/scrape")
def post_web_scraping(payload: ScrapeSchema):
    """
    Envia o cnpj para uma fila que irá fazer o web scraping.
    """
    result_task = scraping_message(payload.cnpj)
    
    return {
        "task_id": result_task
    }

@router.get("/results/{task_id}")
def get_results(task_id):
    """
    Envia o cnpj para uma fila que irá fazer o web scraping.
    """
    tasks_result = celery.AsyncResult(task_id)
    status = tasks_result.status
    result = tasks_result.result if tasks_result.successful() else None
    return {
        "task_id": task_id,
        "task_status": status,
        "result": result
    }
