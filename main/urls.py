from django.urls import path
from . import views
from .views import CarDetailView

urlpatterns = [
    path('inventory', views.index),
    path('sportcars', views.sport),
    path('luxury', views.lux),
    path('suv', views.suv),
    path('about', views.about),
    path('specials', views.specials),
    path('services', views.services),
    path('rent', views.rent),
    path('news', views.news),
    path('locations', views.locations),
    path('contact', views.contact),
    path('sales', views.sales),
    path('inventory/<int:pk>/', CarDetailView.as_view(), name='cars'),
]