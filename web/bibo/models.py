from django.db import models

# Create your models here.

class Zone(models.Model):
    name = models.CharField(max_length = 100)

class Point(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    typ = models.IntegerField()
    zone = models.ForeignKey(Zone)

class Line(models.Model):
    name = models.CharField(max_length = 100)

class LinePoint(models.Model):
    seq = models.IntegerField()
    line = models.ForeignKey(Line)
    point = models.ForeignKey(Point)


class Vehicle(models.Model):
    line = models.ForeignKey(Line)

class Beacon(models.Model):
    name = models.CharField(max_length=50)
    vehicle = models.ForeignKey(Vehicle)

class VehiclePosition(models.Model):
    beacon = models.ForeignKey(Beacon)
    lat = models.FloatField()
    lng = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    money = models.FloatField()

class ProfileInVehicle(models.Model):
    profile = models.ForeignKey(Profile)
    vehicle = models.ForeignKey(Vehicle)
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True, blank=True)

