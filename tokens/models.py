from django.db import models

class Token(models.Model):
    id=models.IntegerField(primary_key=True)
    unique_hash = models.CharField(max_length=20, unique=True)
    tx_hash = models.CharField(max_length=66)
    media_url=models.URLField()
    owner = models.CharField(max_length=42)
