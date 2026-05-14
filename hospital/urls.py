from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('services/', views.services, name='services'),
    path('appointment/', views.appointment, name='appointment'),
    path('appointment/success/<int:id>/', views.appointment_success, name='appointment_success'),
    path('contact/', views.contact, name='contact'),
    path('doctor/<int:id>/', views.doctor_detail, name='doctor_detail'),
]
