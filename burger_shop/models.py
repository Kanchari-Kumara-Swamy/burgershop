from django.db import models

class BurgerModel(models.Model):
 	name = models.CharField(max_length = 100 )
 	price = models.CharField(max_length = 10)

class CustomerModel(models.Model):
	userid = models.CharField(max_length = 100)
	phoneno = models.CharField(max_length = 12)

class OrderModel(models.Model):
	username = models.CharField(max_length = 100)
	phoneno = models.CharField(max_length = 12)
	address = models.CharField(max_length = 100)
	ordereditems = models.CharField(max_length = 100)
	status = models.CharField(max_length = 10)
