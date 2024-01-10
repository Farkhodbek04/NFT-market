from django.shortcuts import render
from .models import Collections, Market

def main(request):
    collections = Collections.objects.all()
    market = Market.objects.all()

    context = {
        'collections': collections,
        'market': market
    }

    return render(request, 'index.html', context)

# Create your views here.
