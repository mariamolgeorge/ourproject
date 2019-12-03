from django.urls import path
from . import views

urlpatterns = [
    path('',views.hrget_home.as_view(),name='hrhome'),
    path('studentregister', views.UserCreate.as_view(), name='studentregister'),
    path('trainerregister', views.TrainerCreate.as_view(), name='trainerregister'),

]
