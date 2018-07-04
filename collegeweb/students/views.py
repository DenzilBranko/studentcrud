from django.shortcuts import render
from django.views import generic
from .models import StudentProfile


class IndexView(generic.ListView):
    template_name = 'students/index.html'
    context_object_name = 'stud_list'

    def get_queryset(self):
        return StudentProfile.objects.all()

class DetailView(generic.DetailView):
    pass















