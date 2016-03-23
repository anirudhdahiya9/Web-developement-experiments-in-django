from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$',views.index,name='index'),
		url(r'^regbike/$',views.regbike,name = 'regbike'),
		url(r'^makebooking/$',views.makebooking,name='makebooking'),
		url(r'^login/$',views.login,name='mylogin'),
		url(r'^register/$',views.register,name='register'),
		]
