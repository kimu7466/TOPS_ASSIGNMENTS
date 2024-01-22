from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.db.models import Q




def is_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if 'email' in request.session:
            return view_func(request, *args, **kwargs)
        else:
            messages.info(request, 'You are not logged in yet.')
            return redirect('login_view')  

    return wrapper

def signup_view(request):
    new_signup = None 
    if request.method == 'POST':
        role_ = request.POST.get("role")
        firstname_ = request.POST.get("firstname").title()
        lastname_ = request.POST.get("lastname").title()
        email_ = request.POST.get("email")
        contact_ = request.POST.get("contact").title()

        if role_ and firstname_ and lastname_ and email_ and contact_:
            try:
                role_instance = Role.objects.get(name=role_)
                new_signup = Signed_up.objects.create(
                    role=role_instance,
                    firstname=firstname_,
                    lastname=lastname_,
                    email=email_,
                    contact=contact_
                )
                new_signup.save()
                messages.success(request, "Successful, Thanks for signing up")
                return redirect("login_view")
            except:
                messages.error(request, "Email already exists. Please use a different email.")
                return redirect("signup_view")

    roles = Role.objects.all()
    return render(request, 'signup.html', {'roles': roles, 'new_signup': new_signup})

def login_view(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        password_ = request.POST['password']
        try:
            get_active_accounts = Signed_up.objects.get(email=email_)

        except Signed_up.DoesNotExist:
            messages.info(request, 'Invalid staff_id or password')
            return redirect('login_view')
        else:
            if get_active_accounts.is_activated == True:
                if password_ == get_active_accounts.password:
                    request.session['email'] = email_
                    request.session['title'] = get_active_accounts.title
                    request.session['id'] = get_active_accounts.id
                    request.session['role'] = get_active_accounts.role.name
                    request.session['firstname'] = get_active_accounts.firstname
                    request.session['lastname'] = get_active_accounts.lastname
                    request.session['gender'] = get_active_accounts.gender
                    request.session['degree'] = get_active_accounts.degree
                    request.session['contact'] = get_active_accounts.contact
                    request.session['address'] = get_active_accounts.address
                    request.session['summary'] = get_active_accounts.summary
                    request.session['is_activated'] = get_active_accounts.is_activated

                    if get_active_accounts.role.name == "Doctor":
                        messages.success(request, f"hello!!! Dr. {get_active_accounts.firstname} {get_active_accounts.lastname}... Now, you are logged in")
                        return redirect('home_view')
                    elif get_active_accounts.role.name == "Patient" :
                        messages.success(request, f"hello!!! Mr. {get_active_accounts.firstname} {get_active_accounts.lastname}... Now, you are logged in")
                        return redirect('home_view')
                else:
                    messages.info(request, 'Invalid staff_id or password')
                    return redirect('login_view')
            else:
                messages.info(request, 'Your account is deactivated. Please contact to Admin.')
                return redirect('login_view')
    return render(request, 'login.html')

@is_authenticated
def home_view(request):
    return render(request, "home.html")

@is_authenticated
def update_profile_view(request):
    if request.method == 'POST':
        title_ = request.POST['title']
        firstname_ = request.POST['firstname']
        lastname_ = request.POST['lastname']
        gender_ = request.POST['gender']
        # email_ = request.POST['email']
        contact_ = request.POST['contact']
        address_ = request.POST['address']
        summary_ = request.POST['summary']

        if request.session.get("role") == "Doctor":
            degree_ = request.POST['degree']

        request.session['title'] = title_
        request.session['firstname'] = firstname_.title()
        request.session['lastname'] = lastname_.title()
        request.session['gender'] = gender_.title()
        # request.session['email'] = email_
        request.session['contact'] = contact_
        request.session['address'] = address_.title()
        request.session['summary'] = summary_.title()

        if request.session.get("role") == "Doctor":
            request.session['degree'] = degree_.upper()

        get_my_detail(request)
        messages.success(request, "Profile updated successfully.")
        return redirect('home_view')


    return render(request, 'update_profile.html')

@is_authenticated
def get_my_detail(request):
    user_id = request.session.get('id')
    my_profile = Signed_up.objects.get(id=user_id)

    my_profile.title = request.session.get('title')
    my_profile.firstname = request.session.get('firstname')
    my_profile.lastname = request.session.get('lastname')
    my_profile.gender = request.session.get('gender')
    # my_profile.email = request.session.get('email')
    my_profile.contact = request.session.get('contact')
    my_profile.address = request.session.get('address')
    my_profile.summary = request.session.get('summary')

    if request.session.get("role") == "Doctor":
        my_profile.degree = request.session.get('degree')

    my_profile.save()

    return

@is_authenticated
def doctor_detail_view(request, doctor_id):
    try:
        doctor = Signed_up.objects.get(id=doctor_id)
        return render(request, 'doctor_detail.html', {'doctor': doctor})
    except Signed_up.DoesNotExist:
        messages.error(request, "Doctor not found.")
        return redirect('all_doctors_view')
    
@is_authenticated
def book_appointment_view(request, doctor_id):
    doctor = get_object_or_404(Signed_up, id=doctor_id)

    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        patient_email = request.POST.get('patient_email')
        patient_contact = request.POST.get('patient_contact')
        doctor_name = request.POST.get('doctor_name')
        doctor_email = request.POST.get('doctor_email')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        additional_info = request.POST.get('additional_info')

        appointment = Appointment.objects.create(   
            patient=patient_name,
            patient_email=patient_email,
            patient_contact=patient_contact,
            doctor=doctor_name,
            doctor_email=doctor_email,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            additional_info=additional_info
        )
        messages.success(request, f"Appointment requested with Dr. {doctor.firstname} {doctor.lastname} on {appointment_date} at {appointment_time}")
        return redirect('my_appointments')

    return render(request, 'book_appointment.html', {'doctor': doctor})

def all_doctors_view(request):
    # Get the ID of the currently logged-in doctor
    logged_in_doctor_id = request.session.get('id')

    # Exclude the currently logged-in doctor from the list
    doctors = Signed_up.objects.filter(role__name="Doctor").exclude(id=logged_in_doctor_id).order_by('-id')

    return render(request, 'all_doctors.html', {'doctors': doctors})

@is_authenticated
def my_appointments(request):
    if request.session.get('role') == "Patient":
        user_email = request.session.get('email')
        appointments = Appointment.objects.filter(patient_email=user_email)
        return render(request, 'view_appointments.html', {'appointments': appointments})
    if request.session.get('role') == "Doctor":
        user_email = request.session.get('email')
        appointments = Appointment.objects.filter(doctor_email=user_email)
        return render(request, 'view_appointments.html', {'appointments': appointments})


@is_authenticated
def update_appointment_status(request, appointment_id):
    if request.method == 'POST':
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.approval_status = not appointment.approval_status
            appointment.save()
            return redirect('doctor_appointments')
        except:
            messages.error(request, "something went wrong try again")
            return redirect('home_view')
    else:
        return redirect('home_view')

def logout(request):
    request.session.clear()
    messages.success(request, "You are logged Out")
    return redirect('login_view')
