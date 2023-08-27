from django.urls import path 
from . import views 

app_name = 'hello'
urlpatterns  = [
    path('', views.index, name = 'index'),
    path('saeed', views.saeed, name = 'saeed'),
    path('javad', views.javad, name = 'javad'),
    path('<str:name>', views.greet, name = 'greet')

]


