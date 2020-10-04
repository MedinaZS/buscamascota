from django.urls import path
from app import views
from buscamascota import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
urlpatterns = [
    path('', views.index, name='index'),
    path('colaborar/', views.colaborate, name='colaborar'),
    path('map/', views.map, name='map'),
    path('publicar/', views.publish, name='publicar'),
    path('terminos/', views.terms, name='terminos'),
    path('licencia/', views.license, name='licencia'),
    path('exito/<int:report_id>', views.success, name='success'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)