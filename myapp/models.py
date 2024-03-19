from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Option(models.Model):
    text = models.CharField(max_length=255)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.text} ({self.marks})"

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    total_score = models.IntegerField(default=0)



    def __str__(self):
        return f"{self.user} - {self.total_score}"
