from django.urls import path
from .import views

app_name = 'blogs'
urlpatterns = [
        path('', views.index, name='index'),
        path('detail/<int:blog_id>/', views.detail, name='detail'),
        ]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
