from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^book/$',views.book, name='book'),
	url(r'^booki/$',views.booki, name='booki'),
	url(r'^manage/$',views.managetrans, name='managetrans')
]
