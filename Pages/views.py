from django.shortcuts import render, redirect
from .models import Team
from Cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.admin import User
from django.contrib import messages
from Contacts.models import Contact
# Create your views here.



def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style',)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    location_search = Car.objects.values_list('city', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        # 'search_fields': search_fields,
        'model_search': model_search,
        'location_search': location_search,
        'body_style_search': body_style_search,
        'year_search': year_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'pages/index.html', data)



def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have made a new inquiry regarding ' + subject
        email_message = f'Thank you {name} for contacting us. We will get back to you soon.' \
                        f' your message was {message} '
        email_host = 'demo.mail.userforinquiry@gmail.com'

        send_mail(
            email_subject,
            email_message,
            email_host,
            [email],
            fail_silently=False,
        )
        messages.success(request, 'Your message has been sent successfully. '
                                  'Please wait for the confirmation through email.')
        return redirect('contact')
    return render(request, 'pages/contact.html')