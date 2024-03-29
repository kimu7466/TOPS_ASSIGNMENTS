from django.db import models
from .utils import generate_uniques
from django.conf import settings
from django.core.mail import send_mail
import random
import string

class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# class Role(BaseClass):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return f'{self.name}'
    
class Role(BaseClass):
    DOCTOR = 'Doctor'
    PATIENT = 'Patient'

    CHOICES = [
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient'),
    ]

    name = models.CharField(max_length=255, choices=CHOICES)

    def __str__(self):
        return f'{self.name}'

class Signed_up(BaseClass):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    title = models.CharField(max_length = 255, blank =True)
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 255,blank = True)
    degree = models.CharField(max_length=255, blank = True)
    email = models.EmailField(max_length = 255, unique=True)
    contact = models.CharField(max_length = 255)
    address = models.TextField(blank = True)
    summary = models.TextField(blank = True)
    otp = models.CharField(max_length=10, default="658734", blank=True)
    password = models.CharField(max_length = 255, blank = True)
    credentials_sent = models.BooleanField(default = False)
    is_activated_patient = models.BooleanField(default = True)
    is_activated_doctor = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.role}"
    
    def save(self, *args, **kwargs):
        if not self.password:
            self.password = generate_uniques.generate_password()

        if not self.credentials_sent:
            name = f"{self.firstname.upper()} {self.lastname.upper()}" 

            subject = f"Login Credentials from | Healthify for {name}"
            message = f"welcome to Healthify You can Login with your Email: {self.email} and password: {self.password}"
            from_email = settings.EMAIL_HOST_USER
            rec_list = [f"{self.email}"]
            
            send_mail(subject,message,from_email,rec_list)

            self.credentials_sent = True

        super(Signed_up, self).save(*args, **kwargs)

class Appointment(BaseClass):
    appointment_number = models.CharField(max_length=255,blank=True)
    patient = models.CharField(max_length=255, blank=True)
    patient_email = models.EmailField(max_length=255,blank=True)
    patient_contact = models.CharField(max_length=255,blank=True)
    doctor = models.CharField(max_length=255,blank=True)
    doctor_email = models.EmailField(max_length=255,blank=True)
    appointment_date = models.DateField(blank=True)
    appointment_time = models.TimeField(blank=True)
    additional_info = models.TextField(blank=True)
    return_message = models.TextField(blank=True)
    approval_status = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.appointment_number} : {self.patient} - {self.doctor} - {self.approval_status}"
    
    def save(self, *args, **kwargs):
        if not self.appointment_number:
            def generate_rest_APN(digit=10):
                APN = string.digits
                number = ""
                for n in range(digit):
                    number += random.choice(APN)
                return number    
                
            self.appointment_number += "APN00"+str(generate_rest_APN()) 

        super(Appointment, self).save(*args, **kwargs)

