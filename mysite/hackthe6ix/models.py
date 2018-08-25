from django.db import models

# Create your models here.
class Listings(models.Model):
    id = models.AutoField(primary_key=True)
    street_name = models.CharField(max_length=30)
    house_number = models.PositiveIntegerField()
    #full_location = house_number + street_name
    price = models.DecimalField(max_digits=5, decimal_places=2)
    lease_length = models.PositiveIntegerField()

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.BooleanField()

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

# class Landlord(models.Model):
    # pId = models.ForeignKey(Person, on_delete=models.CASCADE)

# class Tenants(models.Model):
    # pId = models.ForeignKey(Person, on_delete=models.CASCADE)
