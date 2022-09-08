from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('teams/<str:teamname>', views.team, name='teams'),
    path('yonetim',views.manager, name='managers'),
    path('destekcilerimiz',views.sponsors, name='sponsors'),
    path('basarilarimiz' ,views.achievements, name='achievements'),
    path('etkinliklerimiz', views.events, name='events'),
]