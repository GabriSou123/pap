from django.contrib import admin
from django.urls import path
from app_adocao import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('adotar/', views.adotar, name='adotar'),
    path('contactos/', views.contactos, name='contactos'),
    path('sobreNos/', views.sobreNos, name='sobreNos'),
    path('cao1/', views.cao1, name='cao1'),
    path('cao2/', views.cao2, name='cao2'),
    path('gato4/', views.gato4, name='gato4'),
    
    
]