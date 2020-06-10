from django import forms
from cities.models import City
from .models import Route


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(
        label="From",
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control js-example-basic-single "
                "js-example-basic-single"
            }
        ),
    )
    to_city = forms.ModelChoiceField(
        label="To",
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control js-example-basic-single js-example-basic-single"
            }
        ),
    )
    across_cities = forms.ModelMultipleChoiceField(
        label="Across cities",
        queryset=City.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control js-example-basic-multiple "
                "js-example-basic-multiple"
            }
        ),
    )
    travelling_time = forms.IntegerField(
        label="Train",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Travelling time"}
        ),
    )


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(
        label="Название маршрута",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    from_city = forms.CharField(widget=forms.HiddenInput())
    to_city = forms.CharField(widget=forms.HiddenInput())
    across_cities = forms.CharField(widget=forms.HiddenInput())
    travel_times = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Route
        fields = ("name", "from_city", "to_city", "across_cities", "travel_times")
