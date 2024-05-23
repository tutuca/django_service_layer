from django.contrib import admin
from .models import Fare, Booking, Pax, Buyer


@admin.register(Fare)
class FareAdmin(admin.ModelAdmin):
    ...


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    ...


@admin.register(Pax)
class PaxAdmin(admin.ModelAdmin):
    ...


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    ...


admin.autodiscover()
