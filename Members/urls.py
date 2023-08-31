from django.urls import path
from . import views

urlpatterns = [
    path('',views.member_index,name='member-index'),
    path('member-login/',views.member_login,name='member-login'),
]