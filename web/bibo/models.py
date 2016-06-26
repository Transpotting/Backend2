from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Zone(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Point(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    typ = models.IntegerField(default=0)
    zone = models.ForeignKey(Zone)

    def __str__(self):
        return "%0.6f, %0.6f, %s" % (self.lat, self.lng, str(self.zone))

class Line(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class LinePoint(models.Model):
    seq = models.IntegerField()
    line = models.ForeignKey(Line)
    point = models.ForeignKey(Point)

    def __str__(self):
        return "[%d] %s -> %s" % (self.seq, str(self.line), str(self.point))


class Vehicle(models.Model):
    line = models.ForeignKey(Line)

    def __str__(self):
        return "%s %d" % (str(self.line), self.id)

class Beacon(models.Model):
    name = models.CharField(max_length=50)
    vehicle = models.ForeignKey(Vehicle)

    def __str__(self):
        return "%s %s" % (self.name, str(self.vehicle))

class VehiclePosition(models.Model):
    beacon = models.ForeignKey(Beacon)
    lat = models.FloatField()
    lng = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s %s" % (str(self.lat), str(self.lng), str(self.time))

class Profile(models.Model):
    user = models.ForeignKey(User)
    money = models.FloatField()
    disabled = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

class ProfileInVehicle(models.Model):
    profile = models.ForeignKey(Profile)
    vehicle = models.ForeignKey(Vehicle)
    time_in = models.DateTimeField(auto_now_add=True)
    lat_in = models.FloatField()
    lng_in = models.FloatField()
    time_out = models.DateTimeField(null=True, blank=True)
    lat_out = models.FloatField(null=True, blank=True)
    lng_out = models.FloatField(null=True, blank=True)

    def __str__(self):
        return "%s %s %s %s" % (str(self.profile), str(self.vehicle), str(self.time_in), str(self.time_out))

