from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title
