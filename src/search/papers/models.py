from django.db import models

class Paper(models.Model):
    link = models.CharField(max_length=255)
    summary = models.TextField()
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    date = models.DateField()
    areas = models.CharField(max_length=255)
    fields = models.CharField(max_length=255)
    subjects = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "papers"

    def __str__(self):
        return self.name
# Create your models here.
