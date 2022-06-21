from django.urls import path
from .views import HomeView, SearchView, SearchResultView
urlpatterns = [
    path('', HomeView, name='yts-search-view'),
    path('search', SearchView, name='yts-search-view'),
    path('search/<str:query>', SearchResultView, name='yts-search-result-view')
]