from django.db import models

class User(models.Model):                                            
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    position = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=11)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    address_number = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

class Contact(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)                                            
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    position = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=11)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    address_number = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

class Commentary(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)                                            
    commentary = models.CharField(max_length=250)