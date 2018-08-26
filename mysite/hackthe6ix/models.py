from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, default="dummy")
    password = models.CharField(max_length=30, default="dummy")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=3)
    gender = models.CharField(max_length=10, default="dummy")
    profilepic = models.CharField(max_length=70, default="dummy")

class Listings(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=30)
    price = models.IntegerField(default=40)
    gender = models.CharField(max_length=10, default="dummy")
    lease = models.PositiveIntegerField(default=600)
    phone = models.CharField(max_length=20, default="dummy")
    propertypic = models.CharField(max_length=70, default="dummy")
    description = models.CharField(max_length=300, default="dummy")

class Landlord(models.Model):
	pass
    # pId = models.ForeignKey(Person, on_delete=models.CASCADE)

class Tenants(models.Model):
	pass
    # pId = models.ForeignKey(Person, on_delete=models.CASCADE)
