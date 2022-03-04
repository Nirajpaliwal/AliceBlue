from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from TestAPI.models import Registration, Profile

# Create your views here.


def register(request):
    return render(request, 'registration.html')


def registerUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('psw')

        register = Registration.objects.create(
            name=name, email=email, phone=phone, password=password)
        register.save()
        print(register)

        return render(request, 'profile.html', {'register': register, 'email': email})

    # return HttpResponse('Registered')


def profile(request):
    print(register)
    return render(request, 'profile.html')


def registerProfile(request):
    if request.method == 'POST':
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        state = request.POST.get('state')
        nationality = request.POST.get('nationality')
        register = request.POST.get('register')
        email = request.POST.get('email')
        register = Registration.objects.get(email=email)

        register = Profile.objects.create(gender=gender, dob=dob, address=address,
                                          pincode=pincode, state=state, nationality=nationality, registration=register)
        register.save()

    return render(request, 'login.html')


def login(request):
    return render(request, 'login.html')


def authenticateuser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('psw')

        user = Registration.objects.get(email=email, password=password)
        profile = Profile.objects.get(registration=user)

        userdetails = {
            'user': user,
            'profile': profile
        }

        return render(request, 'userdetails.html', userdetails)

    # return HttpResponse('Incorrect Username and Password')
