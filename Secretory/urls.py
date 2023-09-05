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
    path('manage-events/',views.manage_events, name='manage-events'),
    path('view-event/<int:pk>',views.view_event, name='view-event'),
    path('delete-event/<int:pk>',views.delete_event, name='delete-event'),
    path('add-event/',views.add_event, name='add-event'),
    path('manage-complains/',views.manage_complains, name='manage-complains'),
    path('solve-complain/<int:pk>',views.solve_complain,name='solve-complain'),
    path('view-complain/<int:pk>',views.view_complain,name='view-complain'),
    path('manage-notice/',views.manage_notice, name='manage-notice'),
    path('new-notice/',views.new_notice, name='new-notice'),
]
