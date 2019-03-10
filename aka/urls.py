from django.urls import path
from .views import AkaRedirectView, SearchView, ResultsView

urlpatterns = [
    path('', SearchView.as_view(), name=''),
    path('results', ResultsView.as_view(), name=''),
    path('<str:linklabel>', AkaRedirectView.as_view(), name=''),
]