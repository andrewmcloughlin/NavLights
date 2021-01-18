
from django.contrib import admin
from django.urls import path
from Signal.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', gallery_view, name ='home'),
    path('gallery/', gallery_view, name ='gallery'),
    path('add/', add, name = 'add'),
    path('add', add, name = 'add'),
    path('view/<int:id>/', view, name = 'view'),
    path('update/<int:id>/', update, name = 'update'),
    path('delete/<int:id>/', delete, name = 'delete'),
    path('register/', registerPage, name='register'),
    path('table/', table_view, name='table'),
    path('list/', list_view, name='list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

