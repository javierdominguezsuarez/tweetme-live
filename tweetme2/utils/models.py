from django.db import models

# Create your models here.
class AppBaseModel (models.Model):
    pub = models.DateField("Date of publication",auto_now_add=True)
    hour = models.TimeField("Time of publication", auto_now_add=True)
    class Meta :
        abstract = True
        ordering = ['-pub','-hour']