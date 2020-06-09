from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=99, unique=True, verbose_name="Name route")
    from_city = models.CharField(max_length=99, verbose_name="From")
    to_city = models.CharField(max_length=99, verbose_name="From")
