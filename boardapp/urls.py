from django.urls import path
from .views import signupfnc, loginfnc, listfnc,logoutfnc,detailfnc, goodfnc, readfnc, BoardCreate

urlpatterns = [
    path('signup/', signupfnc, name='signup'),
    path('login/', loginfnc, name='login'),
    path('list/', listfnc, name='list'),
    path('logout/', logoutfnc, name='logout'),
    path('detail/<int:pk>', detailfnc, name='detail'),
    path('good/<int:pk>', goodfnc, name='good'),
    path('read/<int:pk>', readfnc, name='read'),
    path('create/', BoardCreate.as_view(), name='create')
]
