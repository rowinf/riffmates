from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class FeelingChoice(models.TextChoices):
    Happy = "HAPPY"
    Sad = "SAD"
    Neutral = "NEUTRAL"
    Mad = "MAD"
    Other = "OTHER"

class DailyJournal(models.Model):
    date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class FeelingReport(models.Model):
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=False)
    feeling = models.CharField(max_length=20,choices=FeelingChoice.choices)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.ForeignKey(DailyJournal, on_delete=models.CASCADE)

class JournalNote(models.Model):
    date = models.DateField(auto_now_add=True)
    content = models.TextField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.ForeignKey(DailyJournal, on_delete=models.CASCADE)

class JournalTodo(models.Model):
    date = models.DateField(auto_now_add=True)
    priority = models.IntegerField(blank=False)
    content = models.TextField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.ForeignKey(DailyJournal, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
