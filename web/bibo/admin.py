from django.contrib import admin

from .models import *

admin.site.register(Zone)
admin.site.register(Point)
admin.site.register(Line)
admin.site.register(LinePoint)
admin.site.register(Vehicle)
admin.site.register(Beacon)
admin.site.register(VehiclePosition)
admin.site.register(Profile)
admin.site.register(ProfileInVehicle)

