import datetime
from django.db import models
from django.utils import timezone


class Experiment(models.Model):
    experiment_title = models.CharField(max_length=200)
    creator = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date created')

    def __str__(self):
        return self.experiment_title

    def was_created_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_creator(self):
        return self.creator


class Description(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    desc_text = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.desc_text

    def has_been_upvoted(self):
        return self.votes > 0
