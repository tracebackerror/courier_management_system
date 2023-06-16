from django.contrib import admin
from .models import *


class ShipmentAdmin(admin.ModelAdmin):
    readonly_fields = ["booked_by", "created_at", "updated_at"]
    list_display = ["name","picking_city","shipping_city","status","booked_by"]


admin.site.register(Shipment,ShipmentAdmin)
