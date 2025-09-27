from django.urls import path
from . import views

urlpatterns = [
    path('current-stats/', views.current_stats, name='current_stats'),
    path('historical-stats/', views.historical_stats, name='historical_stats')
]