from django.shortcuts import render, redirect
from .models import Thing
from .forms import ThingForm

def home(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})
