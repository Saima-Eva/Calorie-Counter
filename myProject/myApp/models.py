from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    height = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return self.user.username
# models.py



class ConsumedItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    calories_consumed = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.item_name}"
class date_input(models.Model):
    date=models.DateTimeField(default=timezone.now, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)
