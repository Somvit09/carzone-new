from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User


# Create your views here.


def inquiry(request):
    if request.method == "POST":
        car_id = request.POST["car_id"]
        user_id = request.POST["user_id"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        car_title = request.POST["car_title"]
        customer_need = request.POST["customer_need"]
        city = request.POST["city"]
        state = request.POST["state"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        contacts = Contact(
            car_id=car_id,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            car_title=car_title,
            customer_need=customer_need,
            city=city,
            state=state,
            email=email,
            phone=phone,
            message=message,
        )

        send_mail(
            'New Car Inquiry',
            'You have just make a new inquiry for the ' + car_title +
            '. Please wait for the reply from us. We will contact you soon. Have a great day.',
            'demo.mail.userforinquiry@gmail.com',
            [email, ],
            fail_silently=False,
        )
        contacts.save()
        messages.success(request, 'Your message has been sent successfully. '
                                  'Please wait for the confirmation through email.')
        return redirect('/cars/' + car_id)


