from django.urls import path
from core.views import home, about, contact

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about, name='about'),
    path('contact/', contact, name='contact')
]
