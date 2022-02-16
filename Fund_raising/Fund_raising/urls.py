"""Fund_raising URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from users.views import *
from projects.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('handle_login/', handle_login, name='handle_login'),
    path('register/', register, name='register'),
     path('form', hotel_image_view, name = 'form'),
    path('success', success, name = 'success'),
    path('open_login/', open_login, name='open_login'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate,
         name='activate'),
    path('home<id>/', home, name='home'),
    path('profile<id>/', profile, name='profile'),
    path('edit_info<id>/', edit_personal_info, name='edit_info'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)