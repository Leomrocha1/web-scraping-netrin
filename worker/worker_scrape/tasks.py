from worker_scrape import celery


@celery.task(name='web-scraping')
def web_scraping(cnpj):
    """
    Tarefa responsável por fazer o web scraping.
    """
    from worker_scrape import scraping
    try:
        data = scraping.execute_scrape(cnpj)
        return data
    except Exception as e:
        return {"error": str(e)}
