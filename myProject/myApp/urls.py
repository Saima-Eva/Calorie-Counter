from django.urls import path
from myApp.views import *

urlpatterns = [
    path('', register, name='register'),
    path('SignIn/', SignIn, name='SignIn'),
    path('home/', home, name='home'),
    path('logout_f/', logout_f, name='logout_f'),
    path('profile/', profile, name='profile'),
    path('user_profile_update/', user_profile_update, name='user_profile_update'),
    path('consume_calories/', consume_calories, name='consume_calories'),
    path('update_item/<str:id>', update_item, name='update_item'),
    path('delete_item/<str:id>', delete_item, name='delete_item'),
]
