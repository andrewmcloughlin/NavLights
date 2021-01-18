
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from Signal.views import *

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', gallery_view, name ='home'),
    path('gallery/', gallery_view, name ='gallery'),
    path('table/', table_view, name ='table'),
    path('list/', list_view, name ='list'),
    path('Signal/', include('Signal.urls')),
    path('admin/', admin.site.urls),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

