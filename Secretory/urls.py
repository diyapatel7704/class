from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('change-password/',views.change_password, name='change-password'),
    path('edit-profile/',views.edit_profile, name='edit-profile'),
    path('member-details/',views.member_details, name='member-details'),
    path('edit-member/<int:pk>',views.edit_member, name='edit-member'),

]
