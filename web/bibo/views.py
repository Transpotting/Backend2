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



