from django.db import models
from .utils import generate_uniques
from django.conf import settings
from django.core.mail import send_mail



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
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    degree = models.CharField(max_length=255, blank = True)
    email = models.EmailField(max_length = 255, unique=True)
    contact = models.CharField(max_length = 255)
    address = models.TextField(blank = True)
    summary = models.TextField(blank = True)
    password = models.CharField(max_length = 255, blank = True)
    credentials_sent = models.BooleanField(default = False)
    is_activated = models.BooleanField(default = False)


    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.role}"
    
    def save(self, *args, **kwargs):
        if not self.password:
            self.password = generate_uniques.generate_password()

        if self.role.name == "Patient" and self.is_activated == True:
            self.is_activated = True

        if not self.credentials_sent:
            name = f"{self.firstname.upper()} {self.lastname.upper()}" 

            subject = f"Login Credentials from | Healthify for {name}"
            message = f"welcome to Healthify You can Login with your Email: {self.email} and password: {self.password}"
            from_email = settings.EMAIL_HOST_USER
            rec_list = [f"{self.email}"]
            
            send_mail(subject,message,from_email,rec_list)

            self.credentials_sent = True

        super(Signed_up, self).save(*args, **kwargs)






