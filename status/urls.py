from django.urls import path, re_path

from . import views

app_name='status'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^games/(?P<game>[a-z]+)/$', views.game, name='game'),
]
