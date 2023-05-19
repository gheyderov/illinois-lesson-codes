from django.urls import path
from accounts.views import login, register, forget_password, profile, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('forget_password/', forget_password, name='forget_password'),

]
