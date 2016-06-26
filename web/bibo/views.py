from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from .models import *

def index(req):
    ctx = {}
    return render(req, 'bibo/index.html', ctx)


@csrf_exempt
def api_update_position(req):
    result = {}
    if req.method == 'POST':
        name = req.POST['name']
        lat = float(req.POST['lat'])
        lng = float(req.POST['long'])

        beacon = Beacon.objects.get(name = name)
        vehicle = Vehicle.objects.get(beacon = beacon)

        result['ok'] = True
        result['vehicle_id'] = vehicle.id
        
        vp = VehiclePosition(beacon = beacon, lat = lat, lng = lng)
        vp.save()

    else:
        result['ok'] = False
        result['msg'] = "Unsupported method"

    return JsonResponse(result)


@csrf_exempt
def login(req):
    result = {}
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username, password=password)
        if user != None:
            login(req, user)
            p = Profile.objects.get(user = user)
            result['ok'] = True
            result['profile_id'] = p.id
            result['disabled'] = p.disabled
        else:
            result['ok'] = False
            result['msg'] = "Login failed"
    else:
        result['ok'] = False
        result['msg'] = "Unsupported method"
    return JsonResponse(result)


@csrf_exempt
def api_register_with_beacon(req):
    """
    POST parameters:
        * beacon_name
        * profile_id
        * lat
        * lng
    """
    result = {}
    if req.method == 'POST':
        vehicle = Vehicle.objects.get(beacon__name = req.POST['beacon_name'])
        profile = Profile.objects.get(id = req.POST['profile_id'])
        lat = float(req.POST['lat'])
        lng = float(req.POST['lng'])
        piv = ProfileInVehicle(vehicle = vehicle, profile = profile, lat_in = lat, lng_in = lng, pt_in = Point.nearest_point(lat, lng))
        piv.save()
        result['ok'] = True
        result['id'] = piv.id
    else:
        result['ok'] = False
        result['msg'] = "Unsupported method"
    return JsonResponse(result)

@csrf_exempt
def api_unregister_with_beacon(req):
    """
    POST parameters:
        * id (returned from register_with_beacon)
        * lat
        * lng
    """
    result = {}
    if req.method == 'POST':
        piv = ProfileInVehicle.objects.get(id = int(req.POST['id']))
        piv.time_out = datetime.datetime.now()
        lat = float(req.POST['lat'])
        lng = float(req.POST['lng'])
        piv.lat_out = lat
        piv.lng_out = lng
        piv.pt_out = Point.nearest_point(lat, lng)
        piv.save()

