from django.db import models
from django.utils import  timezone
from django.contrib.auth.models import  User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    participant_no = models.IntegerField()
    text = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    photo=models.ImageField(upload_to='photos/',blank=True,null=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.user}-{self.text[:10]}'