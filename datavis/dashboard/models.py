from django.db import models

class PeDeGoiaba(models.Model):
    id = models.IntegerField(primary_key=True)
    valor = models.IntegerField(default=0)