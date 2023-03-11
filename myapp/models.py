from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Package(models.Model):
    image = models.ImageField(blank = True, null = True)
    placeName = models.CharField(max_length = 116)
    description = models.TextField()

    def __str__(self):
        return self.placeName

class PackageSlideImage(models.Model):
    package = models.ForeignKey(Package, on_delete = models.CASCADE)
    image = models.ImageField(blank = True, null = True)

    def __str__(self):
        return self.package.placeName

class Contact(models.Model):
    username = models.CharField(max_length = 116)
    email = models.EmailField()
    content = models.TextField()

    def __str__(self):
        return self.username

tourChoice = [
    (0, 'Only You'),
    (1, 'Family'),
    (2, 'Tour'),
]

transportChoice = [
    (0, 'taxi'),
    (1, 'bus'),
]

accomodationChoice = [
    (0, 'resort'),
    (1, 'hotel'),
]

class Booking(models.Model):
    package = models.ForeignKey(Package, on_delete = models.CASCADE)
    choices = models.IntegerField(default = 0, choices = tourChoice)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    username = models.CharField(max_length = 116, null = True, blank = True)
    email = models.EmailField(null = True, blank = True)
    phoneNumber = models.CharField(max_length = 116)
    transport = models.IntegerField(default = 0, choices = transportChoice)
    accomodation = models.IntegerField(default = 0, choices = accomodationChoice)
    date = models.DateTimeField(auto_now_add = True)