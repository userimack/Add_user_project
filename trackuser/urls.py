from django.conf.urls import url
from trackuser import views

urlpatterns = [
	url(r'^$',views.home,name='home'),
	url(r'^register/$',views.register, name ='register'),
	url(r'^login/$',views.login,name = 'login'),
	url(r'^users/$',views.userlist,name='userlist'),
	url(r'^success/$',views.success,name='success'),
	url(r'^logout/$',views.logout, name='logout'),
	url(r'^profile/$',views.profile,name='profile'),
	url(r'^profile_view/$',views.profile_view,name='profile_view'),
	url(r'^post/$',views.post_list,name='post_list')
	url(r'^post/(?P<pk>[0-9]+/$)',views.post_detail,name='post_detail'),
	url(r'^post/new/$',views.new,name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$',views.post_edit,name='post_edit'),
	]