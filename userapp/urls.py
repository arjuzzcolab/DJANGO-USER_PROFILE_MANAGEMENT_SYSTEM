from django.urls import path
from . import views
urlpatterns = [
 
 path('home',views.show,name='show'),
 path('manage/',views.manage_profile,name='manage'),
 path('register/',views.user_register,name='register'),
 path('',views.user_login,name='login'),
 path('logout/',views.logout,name='logout'),
 path('manage_project/',views.manage_project,name='project'),
 path('portfolio/',views.show_portfolio,name='portfolio'),

]
