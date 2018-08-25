from django.db import models

# Create your models here.
class Listings(models.Model):
    street_name =   models.CharField(max_length=30)
    house_number =  models.PositiveIntegerField()
    #full_location = house_number + street_name
    price =         models.DecimalField(max_digits=5, decimal_places=2)
    lease_length =  models.PositiveIntegerField()

class Landlords(models.Model):
    first_name =    models.CharField(max_length=30)
    last_name =     models.CharField(max_length=30)

class Tenants(models.Model):
    first_name =    models.CharField(max_length=30)
    last_name =     models.CharField(max_length=30)
    