from django.conf import settings
from django.urls import re_path
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^tweets$', views.tweets),
    re_path(r'^create$', views.create),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
