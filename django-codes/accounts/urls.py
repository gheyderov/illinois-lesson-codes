from django.urls import path, re_path, include
from accounts.views import login, register, forget_password, profile, logout, activate

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('forget_password/', forget_password, name='forget_password'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
        activate, name='activate'),
    path('social-auth/', include('social_django.urls', namespace="social")),


]
