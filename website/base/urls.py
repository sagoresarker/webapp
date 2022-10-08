from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('features', views.features, name='features'),
    path('pricing', views.pricing, name='pricing'),
    path('solutions', views.solutions, name='solutions'),
    path('solutions/<str:id>', views.single_solutions, name='single-solutions'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='home')
]