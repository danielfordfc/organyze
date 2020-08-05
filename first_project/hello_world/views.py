from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def base(request):
    my_dict = {'insert_me':"Hello, I am not from views.py"}
    return render(request,'hello_world/index.html',context=my_dict)


def index(request):
    """
    :param request: n/a
    :return: Returns the view based on an HTTP call to the index domain only: i.e. 127.0.0.1:8000

    Similar to how  url(r'^admin/', admin.site.urls) in views.py handles the 127.0.0.1:8000/admin

    """
    my_dict = {'insert_me': "HELLO_WORLD PAGE"}
    return render(request, 'hello_world/index.html', context=my_dict)


def index2(request):
    """
    :param request: n/a
    :return: Returns the view based on an HTTP call to the index domain only: i.e. 127.0.0.1:8000

    Similar to how  url(r'^admin/', admin.site.urls) in views.py handles the 127.0.0.1:8000/admin

    """
    return HttpResponse("<em>Home</em>")#


def help(request):
    help_dict = {'help_message': "Help Page"}
    return render(request, 'hello_world/help.html', context=help_dict)
