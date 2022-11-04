from django.shortcuts import render, HttpResponse
from .models import Login
from django.contrib.auth.hashers import make_password, check_password

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        encryptedpassword=make_password(request.POST['password'])
        print(encryptedpassword)
        checkpassword=check_password(request.POST['password'], encryptedpassword)
        print(checkpassword)
        data=Login(email=email, password=encryptedpassword)

        data.save()
        return HttpResponse('Done')
    else:
        return render(request, 'index.html')