import os

from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


# Create your models here.

# def fileLocation(instance, filename):
#     return 'static/img/car-photos/'.format(instance.car_photo.url, os.path.basename(filename))

class Car(models.Model):
    car_title = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming')
    )
    state = models.CharField(choices=state_choice, max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))
    year = models.IntegerField('year', choices=year_choice)
    conditions = (
        ('Excellent', 'Excellent'),
        ('Out standing', 'Out standing'),
        ('New', 'New'),
        ('Used', 'Used'),
    )
    condition = MultiSelectField(choices=conditions)
    price = models.IntegerField()
    description = RichTextField(max_length=10000)
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )
    features = MultiSelectField(choices=features_choices)
    body_type = (
        ('Sport', 'Sport'),
        ('SUV', 'SUV'),
        ('Mini Van', 'Mini Van'),
        ('Classic', 'Classic'),
        ('Royal', 'Royal'),
    )
    body_style = MultiSelectField(choices=body_type)
    engine = models.CharField(max_length=255)
    transmission_type = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
        ('CVT', 'CVT'),
    )
    transmission = MultiSelectField(choices=transmission_type)
    interior = models.CharField(max_length=255)
    miles = models.FloatField()
    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    door = MultiSelectField(choices=door_choices)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=255)
    millage = models.FloatField()
    fuel_type = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
    )
    fuel = MultiSelectField(choices=fuel_type)
    no_of_owners = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title
