from django.urls import path
from .views import HomeView, SearchView, SearchResultView
urlpatterns = [
    path('', HomeView, name='eztv-search-view'),
    path('search', SearchView, name='eztv-search-view'),
    path('search/<str:query>', SearchResultView, name='eztv-search-result-view')
]