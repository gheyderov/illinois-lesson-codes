from django.urls import path
from accounts.views import login, register, forget_password, profile

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('forget_password/', forget_password, name='forget_password'),

]
