from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=32)
    state = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return "%s - %s" % (self.title, self.state)
