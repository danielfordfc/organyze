from django.conf.urls import url
from hello_world import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^home', views.index2, name='Home'),
    url(r'^help', views.help, name='Help'),
    url(r'^users',views.users,name='Users'),
    url(r'^forms$',views.form_name_view,name='form'),
    url(r'^forms2$',views.modelform_test,name='form2'),
    url(r'^forms3$',views.modelform_user,name='form2')

]