from django.shortcuts import render
from .models import City
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CityForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    # if request.method == 'POST':
    #     form = CityForm(request.POST or None)
    #     if form .is_valid():
    #         print(form.cleaned_data)
    # form = CityForm()
    # cities = City.objects.all()
    cities = City.objects.all()
    paginator = Paginator(cities, 25)
    page = request.GET.get('page')
    cities = paginator.get_page(page)
    return render(request, 'cities/home.html',
                  {'objects_list': cities},)
    # return render(request, 'cities/home.html', {'objects_list': cities, 'form': form})


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('city:home')


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('city:home')


class CityDeleteView(DeleteView):
    model = City
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('city:home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
