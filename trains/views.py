from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .forms import TrainForm
from .models import Train
from django.core.paginator import Paginator
from django.contrib import messages


def home(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 25)
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    return render(request, 'trains/home.html',
                  {'objects_list': trains},)


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('train:home')
    success_message = 'Train successfully created!'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    context_object_name = 'object'
    template_name = 'trains/detail.html'


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('train:home')
    success_message = 'Train successfully updated!'


class TrainDeleteView(DeleteView):
    model = Train
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('city:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Train successfully deleted!')
        return self.post(request, *args, **kwargs)