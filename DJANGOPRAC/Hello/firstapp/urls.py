from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('counter',views.counter,name='counter'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('registerdrive',views.registerdrive,name='registerdrive'),
    path('driverlogin',views.driverlogin,name='driverlogin'),
    path('driverhome',views.driverhome,name='driverhome'),
    path('book_ride',views.book_ride,name='book_ride'),
    path('show_rides',views.show_rides,name='show_rides'),
    path('payment_ride',views.payment_ride,name='payment_ride'),
    path('driver_accept',views.driver_accept,name='driver_accept'),
    path('journey',views.journey,name='journey'),
    path('ride_his',views.ride_his,name='ride_his'),
    path('cancel_ride',views.cancel_ride,name='cancel_ride'),
    path('ratings',views.ratings,name='ratings'),
    path('driver_his',views.driver_his,name='driver_his')

]