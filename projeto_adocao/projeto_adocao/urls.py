from django.contrib import admin
from django.urls import path
from app_adocao import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('adotar/', views.adotar, name='adotar'),
    path('contactos/', views.contactos, name='contactos'),
    path('sobreNos/', views.sobreNos, name='sobreNos'),
    path('animaisadc/<int:animal_id>/', views.animaisadc, name='animais_detalhe'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
