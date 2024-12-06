import os
from celery import Celery
import django
from django.conf import settings
from datetime import timedelta

# Set the default settings module for the 'django' program
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hengampilot.settings")

# Initialize Django setup
django.setup()

# Create an instance of Celery named 'hengampilot'
app = Celery("hengampilot")

# Load the configuration from Django settings
app.config_from_object("django.conf:settings", namespace="CELERY")

# Automatically discover tasks in registered Django app configurations
app.autodiscover_tasks()

# Set the broker URL for Celery to use (e.g., RabbitMQ, Redis)
app.conf.broker_url = settings.CELERY_BROKER_URL

# Retry connection to the broker when Celery starts up
app.conf.broker_connection_retry_on_startup = True

# Define which modules Celery should import tasks from
app.conf.imports = ["shahkar_user.tasks"]

# Set the result backend (e.g., Redis, Database) to store task results
app.conf.result_backend = settings.CELERY_RESULT_BACKEND

# Set the task serialization format (e.g., json, pickle)
app.conf.task_serializer = settings.CELERY_TASK_SERIALIZER

# Set the result serialization format
app.conf.result_serializer = settings.CELERY_RESULT_SERIALIZER

# Define the accepted content types for tasks (here it's only JSON)
app.conf.accept_content = ["json"]

# Set the expiration time for task results (e.g., 1 day)
app.conf.result_expires = timedelta(days=1)

# Set whether tasks are executed immediately for testing (useful in development)
app.conf.task_always_eager = False

# Set the number of tasks that the worker will prefetch before processing
app.conf.worker_prefetch_multiplier = 2
