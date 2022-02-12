from django.shortcuts import render
from users.forms import Register_form


# Create your views here.
def login(request):
    return render(request, 'login.html', )


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

