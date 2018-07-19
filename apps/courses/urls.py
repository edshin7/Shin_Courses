from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^toDestroy/(?P<id>\d+)$', views.toDestroy),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^destroyCourse/(?P<id>\d+)$', views.destroyCourse),
    url(r'^back$', views.back)
]