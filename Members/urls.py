from django.urls import path
from . import views

urlpatterns = [
    path('',views.member_index,name='member-index'),
    path('member-login/',views.member_login,name='member-login'),
    path('member-logout/',views.member_logout,name='member-logout'),
    path('create-complain/',views.create_complain,name='create-complain'),
]