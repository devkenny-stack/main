from django.urls import path
from .views import home, about, admissions, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('admissions/', admissions, name='admissions'),
    path('contact/', contact, name='contact'),
]
