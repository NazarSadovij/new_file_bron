from django.contrib import admin

from BRON_PROJECT.models import Booking, Room, TypeRoom

# Register your models here.
admin.site.register(Room)
admin.site.register(TypeRoom)
admin.site.register(Booking)