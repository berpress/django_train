# Create your models here.
from django.core.exceptions import ValidationError
from django.db import models
from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=99, unique=True, verbose_name="Number train")
    from_city = models.ForeignKey(
        City, on_delete=models.CASCADE, verbose_name="From", related_name="from_city"
    )
    to_city = models.ForeignKey(
        City, on_delete=models.CASCADE, verbose_name="To", related_name="to_city"
    )
    travel_time = models.IntegerField(verbose_name="hours")

    def __str__(self):
        return f"Train {self.name} from {self.from_city} to {self.to_city}"

    class Meta:
        verbose_name = "Train"
        verbose_name_plural = "Trains"
        ordering = ["name"]

    def clean(self, *args, **kwargs):
        if self.to_city == self.from_city:
            raise ValidationError("Check city")
        qs = Train.objects.filter(
            from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_time
        ).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("Change time")
        return super(Train, self).clean(*args, **kwargs)
