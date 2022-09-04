from django.urls import path
from book import views

urlpatterns = [
    path('signin/', views.login, name='login'),
    path('signup/', views.signup, name='register'),
    path('home/', views.home, name='home'),
    path('viewcart/', views.viewcart, name='viewcart'),
    path('logout/', views.logout, name='logout'),

]
