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
    email = models.CharField(max_length=50, default="dummy")
    password = models.CharField(max_length=30, default="dummy")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.BooleanField()
    profilepic = models.CharField(max_length=70, default="dummy")


class Landlord(models.Model):
	pass
    # pId = models.ForeignKey(Person, on_delete=models.CASCADE)

class Tenants(models.Model):
	pass
    # pId = models.ForeignKey(Person, on_delete=models.CASCADE)
