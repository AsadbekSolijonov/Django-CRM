from django.urls import path
from website.views import index, logout_user, register

urlpatterns = [
    path('',  index, name='index'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register')
]