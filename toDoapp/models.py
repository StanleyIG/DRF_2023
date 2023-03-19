from django.db import models
from authapp.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    repository_link = models.URLField(blank=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name



class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField("active", default=True)


