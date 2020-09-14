from django.db import models


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120, verbose_name="Название")
    description = models.CharField(max_length=120, verbose_name="Описание")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Todos"
