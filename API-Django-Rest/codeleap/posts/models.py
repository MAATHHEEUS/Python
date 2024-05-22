from uuid import uuid4
from django.db import models

# Create your models here.
class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=255, editable=False)
    created_datetime = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
