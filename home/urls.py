from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
    url(r'^login/', views.login, name='login'),
    url(r'^profile/', views.profile, name='profile'),
)