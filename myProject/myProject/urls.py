"""
URL configuration for md_asaduzzaman_calorie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myApp.urls')),
    
    # path('', register, name='register'),
    # path('SignIn/', SignIn, name='SignIn'),
    # path('home/', home, name='home'),
    # path('logout_f/', logout_f, name='logout_f'),
    # path('profile/', profile, name='profile'),
    # path('user_profile_update/', user_profile_update, name='user_profile_update'),
    # path('consume_calories/', consume_calories, name='consume_calories'),
    # path('update_item/<str:id>', update_item, name='update_item'),
    # path('delete_item/<str:id>', delete_item, name='delete_item'),
]
