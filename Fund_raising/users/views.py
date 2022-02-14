from django.shortcuts import render
from users.forms import Register_form
from .models import Users



# Create your views here.


def handle_login(request):
    users= Users.objects.all()
    email = request.GET['email']
    password = request.GET['psw']

    for user in users:
        if user.email == email and user.password == password:
            current_user = {'user': user}
            return render(request, 'home.html', current_user)

        else:

            return render(request, 'login.html')

def open_login(request):
    return render(request, 'login.html')




def register(request):
    if request.method == 'GET':
        form_dict = {}
        form = Register_form()
        form_dict['form'] = form
        return render(request, 'register.html', form_dict)
    else:
        if request.method == 'POST':
            form_dict = {}
            form = Register_form(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'login.html', form_dict)
            else:
                form_dict['form'] = form
                return render(request, 'register.html', form_dict)


def open_profile(request):

    return render(request, 'profile.html')




