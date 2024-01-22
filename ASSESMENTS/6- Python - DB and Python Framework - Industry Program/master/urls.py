from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('signup_view/', signup_view, name='signup_view'),
    path('home_view/', home_view, name='home_view'),
    path('all_doctors_view/', all_doctors_view, name='all_doctors_view'),
    path('doctor_detail_view/<int:doctor_id>/', doctor_detail_view, name='doctor_detail_view'),
    path('book_appointment_view/<int:doctor_id>/', book_appointment_view, name='book_appointment_view'),
    path('my_appointments/', my_appointments, name='my_appointments'),
    path('update_profile_view/', update_profile_view, name='update_profile_view'),
    path('logout/', logout, name='logout'),
    path('update_appointment_status/<int:appointment_id>/', update_appointment_status, name='update_appointment_status'),

]
