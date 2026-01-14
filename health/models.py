from django.db import models
from .validators import leao_nao

class Todo(models.Model):
    title = models.CharField(max_length=200, validators=[leao_nao])
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title