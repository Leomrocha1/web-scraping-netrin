from worker_scrape import celery

if __name__ == '__main__':
    argv = [
        'worker',
        '--loglevel=INFO',
        '--concurrency=1',
    ]

    celery.worker_main(argv)
