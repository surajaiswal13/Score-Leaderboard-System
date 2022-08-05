from django.db import models

# Create your models here.
class LeaderBoard(models.Model):
    '''
    LeaderBoard Model
    '''

    user = models.CharField(max_length=50)
    score = models.IntegerField()
    timestamp = models.DateTimeField()