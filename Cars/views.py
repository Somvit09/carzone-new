from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Car


# Create your views here.

def cars(request):
    car = Car.objects.order_by('-created_date')
    page_to_be_shown = Paginator(car, 2)
    page = request.GET.get('page')
    paged_cars = page_to_be_shown.get_page(page)
    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style',)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    location_search = Car.objects.values_list('city', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    data = {
        'car': paged_cars,
        # 'search_fields': search_fields,
        'model_search': model_search,
        'location_search': location_search,
        'body_style_search': body_style_search,
        'year_search': year_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'cars/cars.html', data)


def car_details(request, id):
    sample_car = get_object_or_404(Car, pk=id)
    data = {
        'sample_car': sample_car,
    }
    return render(request, 'cars/car-details.html', data)


def search(request):
    # car = get_object_or_404(Car, pk=id)
    cars = Car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)
    if 'city' in request.GET:
        location = request.GET['city']
        if location:
            cars = cars.filter(city__iexact=location)
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact=transmission)
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style',)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    location_search = Car.objects.values_list('city', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
    data = {
        # 'car': car,
        'cars': cars,
        # 'search_fields': search_fields,
        'model_search': model_search,
        'location_search': location_search,
        'body_style_search': body_style_search,
        'year_search': year_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'cars/search.html', data)