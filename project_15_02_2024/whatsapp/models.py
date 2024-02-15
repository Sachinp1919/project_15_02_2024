from django.db import models

class Whatsapp(models.Model):
    contact_list = models.CharField(max_length=30)
    status_list = models.IntegerField()
    chat = models.CharField(max_length=20)
    group_list = models.IntegerField()
