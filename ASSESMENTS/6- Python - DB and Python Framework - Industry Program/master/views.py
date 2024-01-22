from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages




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
        firstname_ = request.POST.get("firstName")
        lastname_ = request.POST.get("lastName")
        email_ = request.POST.get("email")
        contact_ = request.POST.get("contact")

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
                    request.session['id'] = get_active_accounts.id
                    request.session['role'] = get_active_accounts.role.name
                    request.session['firstname'] = get_active_accounts.firstname
                    request.session['lastname'] = get_active_accounts.lastname
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

# @is_authenticated
# def doctor_detail_view(request,doctor_id):
#     doctor = signup_view.objects.get(id = doctor_id)
#     return render(request, 'doctor_detail.html',{'doctor': doctor})

@is_authenticated
def doctor_detail_view(request, doctor_id):
    try:
        doctor = Signed_up.objects.get(id=doctor_id)
        return render(request, 'doctor_detail.html', {'doctor': doctor})
    except Signed_up.DoesNotExist:
        messages.error(request, "Doctor not found.")
        return redirect('all_doctors_view')
    
@is_authenticated
def update_profile_view(request):
    return render(request, 'update_profile.html')


@is_authenticated
def home_view(request):
    return render(request, "home.html")

def all_doctors_view(request):
    doctors = Signed_up.objects.filter(role__name="Doctor").order_by('-id')
    return render(request, 'all_doctors.html', {'doctors': doctors})

def logout(request):
    request.session.clear()
    messages.success(request, "You are logged Out")
    return redirect('login_view')
