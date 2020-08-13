from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from hello_world.forms import ModelFormTest, ModelFormUser



from hello_world.models import Topic, Webpage, AccessRecords, User, Task


# Create your views here.

def modelform_test(request):
    f = ModelFormTest()
    if request.method == 'POST':
        f = ModelFormTest(request.POST)
        new_article = f.save()

    return render(request, 'hello_world/form_page2.html', context={'form': f})

def modelform_user(request):
    f = ModelFormUser()
    if request.method == 'POST':
        f = ModelFormUser(request.POST)
        f.save()

    return render(request, 'hello_world/form_page3.html', context={'form': f})




def form_name_view(request):

    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success")
            print('Name: ' + str(form.cleaned_data['name']))
            print('Task: ' + str(form.cleaned_data['task']))
            print('start_date: ' + str(form.cleaned_data['start_date']))

    return render(request,'hello_world/form_page.html',context={'form':form})


def base(request):

    webpage_list = AccessRecords.objects.order_by('date')
    date_dict = {'access_records': webpage_list}


    my_dict = {'insert_me':"Hello, I am not from views.py"}
    return render(request,'hello_world/index.html',context=date_dict)


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


def users(request):
    """
    :param request: n/a
    :return: Returns the view based on an HTTP call to the index domain only: i.e. 127.0.0.1:8000

    Similar to how  url(r'^admin/', admin.site.urls) in views.py handles the 127.0.0.1:8000/admin

    """

    user_list = Task.objects.order_by('username')
    user_dict = {'user_dict': user_list}
    return render(request, 'hello_world/sidebar2_django.html', context=user_dict)
