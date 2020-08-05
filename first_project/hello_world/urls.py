from django.conf.urls import url
from hello_world import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^home', views.index2, name='Home'),
    url(r'^help', views.help, name='Home')

]