from django.db import models

class Emotion(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]