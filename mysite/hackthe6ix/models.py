from django.db import models

# Create your models here.
class Listings(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=30)
    price = models.IntegerField()
    gender = models.CharField(max_length=10, default="dummy")
    lease = models.PositiveIntegerField()
    phone = models.CharField(max_length=20, default="dummy")
    propertypic = models.CharField(max_length=70, default="dummy")

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, default="dummy")
    password = models.CharField(max_length=30, default="dummy")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, default="dummy")
    profilepic = models.CharField(max_length=70, default="dummy")

class Landlord(models.Model):
	pass
    # pId = models.ForeignKey(Person, on_delete=models.CASCADE)

class Tenants(models.Model):
	pass
    # pId = models.ForeignKey(Person, on_delete=models.CASCADE)
