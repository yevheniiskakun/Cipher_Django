from django.db import models

class Encryption_method(models.Model):
  name = models.CharField(max_length=100, default="")
  description = models.CharField(max_length=300, default="")

  def __str__(self):
    return self.name
