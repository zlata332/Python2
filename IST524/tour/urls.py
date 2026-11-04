from django.urls import path
from . import views
from .models import Tour

urlpatterns = [
    path('tour_list/', views.tour_list_view, name='tour_list'),
    path('tour/<int:tour_id>/', views.tour_detail_view, name='tour_detail'),
]