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
from django.urls import path,include
from users.views import *
from projects.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('form',UserProjectCreateView.as_view(), name = ''),
    path('',project_list, name='project_list'),
    path('',include("django.contrib.auth.urls")),
    path('<int:id>',project_details, name='project_details'),
    path('<int:project_id>/donate/',donate, name='donate'),     
    path('<int:id>/report_p',report_p,name='report_p'),
    path('<int:id>/project_rating',project_rating,name='project_rating'),
    path('<int:id>/add_rate',add_rate,name='add_rate'),
    path('handle_login/', handle_login, name='handle_login'),
    path('register/', register, name='register'),
    path('open_login/', open_login, name='open_login'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate,
         name='activate'),
    path('home/', home, name='home'),
    path('profile<id>/', profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


   
