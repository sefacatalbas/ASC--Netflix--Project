import imp
from django.urls import path  #varan 24
from .views import * #varan 25 

urlpatterns =[  #varan 26 
    path('register/',userRegister, name='register'),
    path('login/', userLogin, name='login'), #Varan 43..
    path('logout/', userLogout, name='logout'), #Varan 44 logout onceden yazıldı hazır olsun diye...
    path('profile/', profile, name='profile'), # Varan 52
    path('create/', createProfile, name='create'), #Varan 63
    path('hesap/', hesap, name="hesap"),
    path('delete/', userDelete, name="delete"),
    path('update/', update, name='update'),

]