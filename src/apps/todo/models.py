from django.db import models


class TimestampedModel(object):
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class Project(TimestampedModel, models.Model):
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)


class Milestone(TimestampedModel, models.Model):
    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project, related_name='milestones')


class Ticket(TimestampedModel, models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)
    project = models.ForeignKey(Project, related_name='tickets')



