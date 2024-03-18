from django.urls import path 
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('details/<int:id>',views.details,name='details'),
    path('register/',views.register,name='register'),
    path('login/',views.loginn,name='login'),
    path('logout/',views.logoutt,name='logout')
   
    
]