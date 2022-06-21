from django.shortcuts import redirect, render
from django.urls import reverse
from ayeaye.api import yts_search
from django.http import JsonResponse

# Create your views here.

def HomeView(request):
    return redirect(reverse('yts-search-view'))

def SearchView(request):
    return render(request, 'base.html')

def SearchResultView(request, query):
    results = yts_search(query)

    return render(request, 'search-results.html', context={'data':results, 'service_name':'yts'})