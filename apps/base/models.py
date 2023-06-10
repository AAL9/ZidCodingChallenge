from django.db import models

# Create your models here.
class Order(models.Model):
    productName = models.CharField(max_length=200)
    customerName = models.CharField(max_length=200, null=False, default='')
    customerNumber = models.CharField(max_length=200, null=False, default='')
    orderCreated = models.DateTimeField(auto_now_add=True)
    shippingFrom = models.CharField(max_length=200)
    shippingTo = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    courier = models.CharField(max_length=200, blank=True)
    policyNum = models.CharField(max_length=200, blank = True)
    waybillCreated = models.BooleanField(default=False)


class Smsa(models.Model):
    policyNum = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    shippingFrom = models.CharField(max_length=200)
    senderName = models.CharField(max_length=200)
    senderNumber = models.CharField(max_length=200)
    shippingTo = models.CharField(max_length=200)
    receiverName = models.CharField(max_length=200)
    receiverNumber = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    canBeCanceled = models.BooleanField(default=False)

class Aramex(models.Model):
    policyNum = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    shippingFrom = models.CharField(max_length=200)
    senderName = models.CharField(max_length=200)
    senderNumber = models.CharField(max_length=200)
    shippingTo = models.CharField(max_length=200)
    receiverName = models.CharField(max_length=200)
    receiverNumber = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    canBeCanceled = models.BooleanField(default=True)

class SPL(models.Model):
    policyNum = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    shippingFrom = models.CharField(max_length=200)
    senderName = models.CharField(max_length=200)
    senderNumber = models.CharField(max_length=200)
    shippingTo = models.CharField(max_length=200)
    receiverName = models.CharField(max_length=200)
    receiverNumber = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    canBeCanceled = models.BooleanField(default=True)