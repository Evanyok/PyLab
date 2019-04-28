# Celery
Celery is a task queue. Here I will use it to integrate with django and rabbitmq to construct a asynchronize web structure.

1. install celery
    - install celery library
        <p>
        <code>
            $ pip install celery
        </code>
        </p>
    - install redis library, used to save result
        <p>
        <code>
            $ pip install redis
        </code>
        </p>
2. usage
    - define task, reference <a href="#">lab/celery/tasks.py</a>
    - run task
        <p>
        <code>
            $ celery -A tasks worker --loglevel=info
        </code>
        </p>
    - check result
        <p>
        <code>
            $ python test.py
        </code>
        </p>
    