from django.contrib.auth.views import LoginView, LogoutView

from django.urls import path, include
from .views import *



app_name = "records"
urlpatterns = [
    path('', ServiceListView.as_view(), name='records_list',),
    path('create/', recordCreatView.as_view(), name='record_create'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
