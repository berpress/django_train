from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    name = "Bob"
    context = {'name': name}
    return render(request, 'hello.html', context)
