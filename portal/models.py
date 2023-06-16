from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User

STAIUS_CHOICES = (
    ("Order Booked","Order Booked"),
    ("Collected From Sender","Collected From Sender"),
    ("In Transit","In Transit"),
    ("Transit","Transit"),
    ("Received To Nearest Hub","Received To Nearest Hub"),
    ("Shipment Delivered","Shipment Delivered")
)

class Shipment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_no = models.PositiveBigIntegerField()
    picking_address = models.CharField(max_length=500)
    picking_city = models.CharField(max_length=155)
    picking_pincode = models.PositiveIntegerField()
    picking_date = models.DateField()
    shipping_address = models.CharField(max_length=500)
    shipping_city = models.CharField(max_length=155)
    shipping_pincode = models.PositiveIntegerField()
    goods_weight = models.CharField(max_length=255)
    courier_type = models.CharField(max_length=255)
    fast_delivery = models.BooleanField(default=False)
    total_fare = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STAIUS_CHOICES, default="Order Booked")
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name