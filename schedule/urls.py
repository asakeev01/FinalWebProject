from django.urls import path, include

from .views import *

urlpatterns = [
    path('', departments_list, name = 'departments'),
    path('<int:pk>', department, name = 'department')
]