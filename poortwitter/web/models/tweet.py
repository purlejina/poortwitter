from django.db import models

class Tweet(models.Model):
    name = models.CharField(verbose_name='name', null=True, blank=True, max_length=25)
    message = models.CharField(verbose_name='message', null=True, blank=True, max_length=50)
    datetime = models.DateTimeField(verbose_name='datetime', auto_now_add=True, null=True, blank=True)
