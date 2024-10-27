from django.db import models
from django.contrib.admin.models import LogEntry

# Create your models here.

class ActionHistory(LogEntry):
    class Meta:
        proxy = True