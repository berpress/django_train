from django.shortcuts import render
from .models import Train
# from django.views.generic import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .forms import CityForm
# from django.urls import reverse_lazy
from django.core.paginator import Paginator
# from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib import messages
# Create your views here.


def home(request):
    # if request.method == 'POST':
    #     form = CityForm(request.POST or None)
    #     if form .is_valid():
    #         print(form.cleaned_data)
    # form = CityForm()
    # cities = City.objects.all()
    trains = Train.objects.all()
    paginator = Paginator(trains, 25)
    page = request.GET.get('page')
    cities = paginator.get_page(page)
    return render(request, 'trains/home.html',
                  {'objects_list': trains},)
    # return render(request, 'cities/home.html', {'objects_list': cities, 'form': form})
