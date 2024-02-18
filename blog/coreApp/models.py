from django.db import models

# Create your models here.
class IndexPage(models.Model):
    banner = models.CharField(max_length=200, unique=False, default='مرحبا بكم')

    def __str__(self):
        return self.banner