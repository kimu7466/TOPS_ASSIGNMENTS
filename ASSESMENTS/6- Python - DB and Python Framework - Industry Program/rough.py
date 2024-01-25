
# def forget_password_view(request):
#     if request.method == "POST":  
#         email_ = request.POST.get('email').lower()   #1
#         try:
#             check_user = Signed_up.objects.get(email=email_)
#             print(f'this is check_user : {check_user.email}')
#         except Signed_up.DoesNotExist:
#             messages.info(request, "User doesn't exist")
#             return redirect('login_view')

#         try:
#             if check_user:

#                 otp = generate_uniques.generate_otp()
#                 print(otp)
#                 subject = "OTP for [Forget Password]"
#                 message = f"OTP for reseting your password is : {otp}"
#                 from_email = settings.EMAIL_HOST_USER
#                 recipient_list = [email_]

#                 check_user.otp = otp

#                 check_user.save()

#                 send_mail(subject, message, from_email, recipient_list)
                
#                 context = {'email':email_,'check_user':check_user}
#                 return render(request, 'otp_verification.html', context)
            
#             else:
#                 messages.error(request, "User does not exist, create a new account or Input correct Email of registered account")
#                 return redirect('forget_password_view')

#         except:
#             messages.error(request, "User does not exist, create a new account or Input correct Email of registered account")
#             return redirect('forget_password_view')
#     return render(request, 'forget_password.html')

# def otp_verification_view(request):
#     if request.method == 'POST':
#         email_ = request.POST.get('email')

#         print(f'this is the hidden email in form : {email_}')
        

#         otp_ = request.POST.get('otp')
#         print(f'this is the otp in form : {otp_}')


#         new_password = request.POST.get('new_password')
#         confirm_password = request.POST.get('confirm_password')

#         checkuser = Signed_up.objects.filter(email=email_).first()
#         print(f"this is a checkuser otp : {checkuser.otp}")

#         try:
#             if checkuser.otp == otp_:
#                 print("otp match")

#                 if new_password == confirm_password:
#                     print("password match")
#                     checkuser.password = new_password
#                     checkuser.save()
#                     messages.success(request, "Password reseted successfully")
#                     return redirect('login_view')
                
#                 if new_password != confirm_password:
#                     print("password mismatch")
            
#             if checkuser.otp != otp_:
#                 print("otp mismatch")

#         except:
#             messages.error(request, "something went wrong try again")
#             return redirect('forget_password_view')
#     return render (request, "otp_verification.html")

# def resend_otp(request):
#     if request.method == "POST":
#         otp_email = request.POST.get('email').lower()
#         try:
#             check_user = Signed_up.objects.get(email = otp_email)

#             if check_user:
#                 otp = generate_uniques.generate_otp()
#                 print(otp)
#                 subject = "OTP for [Forget Password]"
#                 message = f"OTP for reseting your password is : {otp}"
#                 from_email = settings.EMAIL_HOST_USER
#                 recipient_list = [otp_email]

#                 check_user.otp = otp

#                 check_user.save()

#                 send_mail(subject, message, from_email, recipient_list)
                
#                 context = {'email':otp_email,'check_user':check_user}
#                 return render(request, 'otp_verification.html', context)
            
#             else:
#                 messages.error(request, "User does not exist, create a new account or Input correct Email of registered account")
#                 return redirect('forget_password_view')

#         except:
#             messages.error(request, "User does not exist, create a new account or Input correct Email of registered account")
#             return redirect('forget_password_view')
#     return render(request, 'forget_password.html')


###################>>>>>>>>>>>>>>>>>>

