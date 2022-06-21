from django.shortcuts import redirect, render
from django.urls import reverse
from ayeaye.api import eztv_search
from django.http import JsonResponse

# Create your views here.

def HomeView(request):
    return redirect(reverse('eztv-search-view'))

def SearchView(request):
    return render(request, 'base.html')

def SearchResultView(request, query):
    results = eztv_search(query)
    print(len(results))
    return render(request, 'search-results.html', context={'data':results, 'service_name':'eztv'})