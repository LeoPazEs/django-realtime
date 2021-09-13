from django.urls import path 

from .views import IndexView, SalaView 

urlpatterns = {
    path('',IndexView.asView(), name= 'index'), 
    path('chat/<str:nome_sala>',SalaView.asView(),name= 'sala'),
}