from django.db import models
from trains.models import Train


class Route(models.Model):
    name = models.CharField(max_length=99, unique=True, verbose_name="Name route")
    from_city = models.CharField(max_length=99, verbose_name="From")
    to_city = models.CharField(max_length=99, verbose_name="From")
    across_cities = models.ManyToManyField(
        Train, blank=True, verbose_name="Across cities"
    )
    travel_times = models.IntegerField(verbose_name="Travels times")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routers"
        ordering = ["name"]
