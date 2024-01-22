from django.shortcuts import render, redirect
from master.models import Signed_up, Appointment
from django.contrib import messages

def approve_appointment_view(request, appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.approval_status = True
        appointment.save()

        messages.success(request, "Appointment approved successfully.")
        return redirect('appointments_list_view')
    except Appointment.DoesNotExist:
        messages.error(request, "Appointment not found.")
        return redirect('appointments_list_view')

def appointments_list_view(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments_list.html', {'appointments': appointments})
