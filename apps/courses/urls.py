from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/add$', views.add),
    url(r'^courses/(?P<id>\d+)$', views.show),
    url(r'^courses/(?P<id>\d+)/destroy$', views.destroy),
    url(r'^courses/(?P<id>\d+)/confirm_delete$', views.confirm_delete),
    url(r'^courses/(?P<id>\d+)/comment$', views.add_comment)
]
