from django.contrib import admin
from django.urls import path
from app_adocao import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('adotar/', views.adotar, name='adotar'),  # lista de animais
    path('contactos/', views.contactos, name='contactos'),
    path('sobreNos/', views.sobreNos, name='sobreNos'),
    path('cao1/', views.cao1, name='cao1'),
    path('gato4/', views.gato4, name='gato4'),
    path('animaisadc/<int:animal_id>/', views.animaisadc, name='animais_detalhe'),  # detalhe do animal
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
