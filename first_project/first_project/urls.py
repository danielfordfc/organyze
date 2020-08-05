"""first_project URL Configuration


The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from hello_world import views
from django.conf.urls import include




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.base, name='base'),
    url(r'^hello_world/', include('hello_world.urls'))

]

'''
url(r'^hello_world/', include('hello_world.urls'))
essentially redirects the page calls to be handled inside hello_world/urls.py. In which the views are defined
inside that file and now include /hello_world/ from the root domain. 

i.e. index page now sits on 127.0.0.1:8000/hello_world
'''