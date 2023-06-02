from django.urls import path
from core.views import home, about, contact, ContactView

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about, name='about'),
    path('contact/', ContactView.as_view(), name='contact')
]
