from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=100)


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=100)
    count = models.IntegerField()
