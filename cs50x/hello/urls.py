from django.urls import path 
from . import views 

urlpatterns  = [
    path('', views.index, name = 'index'),
    path('saeed', views.saeed, name = 'saeed'),
    path('javad', views.javad, name = 'javad'),
    path('<str:name>', views.greet, name = 'greet')

]


