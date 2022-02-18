from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from users.forms import Register_form, Update_form
from .models import Users
from .tokens import account_activation_token


# Create your views here.
def handle_login(request):
    users = Users.objects.all()
    email = request.GET['email']
    password = request.GET['psw']
    for user in users:
        if user.email == email and user.password == password:
            if user.is_active:
                dict = {'user': user}
                return render(request, 'home.html', dict)
            else:
                args = {'error': "Please active your account"}
                return render(request, 'login.html', args)

    args = {'error': "User not found"}
    return render(request, 'login.html', args)


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
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activation link has been sent to your email id'
                message = render_to_string('acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'id': urlsafe_base64_encode(force_bytes(user.id)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                return render(request, 'login.html', form_dict)
            else:
                form_dict['form'] = form
                return render(request, 'register.html', form_dict)


def edit_personal_info(request, id):
    user = Users.objects.get(id=id)
    if request.method == "GET":
        form_dict = {'user': user}
        form = Update_form(instance=user)
        form_dict['form'] = form
        return render(request, 'edit_personal_info.html', form_dict)
    else:
        form = Update_form(request.POST, instance=user)
        form.save()
        dict = {'user': user}
        return render(request, 'profile.html', dict)


def activate(request, uidb64, token):
    try:
        user = Users.objects.get(id=uidb64)
    except(TypeError, ValueError, OverflowError):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def home(request, id):
    user = Users.objects.get(id=id)
    dict = {'user': user}
    return render(request, 'home.html', dict)


def profile(request, id):
    user = Users.objects.get(id=id)
    dict = {'user': user}
    return render(request, 'profile.html', dict)


def delete_acc(request, id):
    Users.objects.filter(id=id).delete()
    return render(request, 'login.html')

