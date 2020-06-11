from django.shortcuts import render
from .forms import RouteForm
from django.contrib import messages


def home(request):
    form = RouteForm()
    return render(request, "routes/home.html", {"form": form})


def find_routes(request):
    if request.method == "POST":
        form = RouteForm(request.POST or None)
        if form.is_valid():
            pass
            # data = form.changed_data
        return render(request, "routes/home.html", {"form": form})
    else:
        messages.error(request, "You mast create route")
        form = RouteForm()
        return render(request, "routes/home.html", {"form": form})
