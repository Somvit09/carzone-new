from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from Contacts.models import Contact
from django.contrib.auth.decorators import login_required


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        current_user = auth.authenticate(
            username=username,
            password=password,
        )
        if current_user is not None:
            auth.login(request, current_user)
            messages.success(request, ': User logged in successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Incorrect Credentials, please try again.')
            return redirect('login')
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('login')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists.')
                    return redirect('login')
                else:
                    new_user = User.objects.create_user(
                        username=username,
                        first_name=firstname,
                        last_name=lastname,
                        email=email,
                        password=password,
                    )
                    new_user.save()
                    auth.login(request, new_user)
                    messages.success(request, ': User registered successfully.')
                    return redirect('dashboard')
        messages.error(request, 'Password does not match.')
    return render(request, 'accounts/signup.html')


@login_required(login_url='login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-created_date').filter(user_id=request.user.id)
    data = {
        'user_inquiry': user_inquiry,
    }
    return render(request, 'accounts/dashboard.html', data)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')
