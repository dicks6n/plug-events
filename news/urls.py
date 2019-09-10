from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url('^$', views.home, name='home'),
    url(r'about/', views.about, name='about'),
]