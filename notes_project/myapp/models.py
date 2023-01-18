from django.db import models

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    task = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'entry '+ str(self.id)
