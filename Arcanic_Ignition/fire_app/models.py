from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class CustomerMessage(models.Model):
    contact = models.CharField(max_length=30)
    text = models.CharField(max_length=2000)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


