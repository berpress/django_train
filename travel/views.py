from django.shortcuts import render


def home_view(request):
    name = "Alexander"
    context = {"name": name}
    return render(request, "hello.html", context)
