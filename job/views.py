from django.shortcuts import render
from .models import Job
from personals.models import Personal
# Create your views here.


def home(request):
    jobs = Job.objects
    personals = Personal.objects
    return render(request, 'job/home.html', {'jobs': jobs, 'Personal': personals})

