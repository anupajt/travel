

from .import views
from django.urls import path

urlpatterns=[
    path('register1',views.register1,name='register1'),
    path('login1',views.login1,name='login1'),
    path('logout',views.logout,name='logout'),
]