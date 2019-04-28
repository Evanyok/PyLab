from celery import Celery

# Name of task queue: tasks
# Broker middleware: rabbitmq
# Backend(Save) middleware: redis
app = Celery('tasks', backend="redis://localhost", broker="amqp://localhost")

@app.task
def add(x, y):
    return x + y