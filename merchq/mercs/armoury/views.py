from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import render, get_object_or_404

from mercs.forces.models import Force
from mercs.armoury.models import VehicleType

def index(request):
    forces = Force.objects.all().annotate(vehicle_count = Count('vehicle'))
    context = {'forces': forces}

    return render(request, 'armoury/index.html', context)

def force_armoury(request, force_id):
    force = get_object_or_404(Force, id=force_id)

    vehicles = force.vehicle_set.all().order_by('vehicle_type',
                                                'vehicle_weight',
                                                'vehicle_name')

    vehicle_types = VehicleType.objects.all().order_by('type_name')

    maintenance_cost = sum([vehicle.weekly_maintenance_cost for vehicle
                            in vehicles])

    support = sum([vehicle.weekly_support for vehicle
                   in vehicles])

    vehicle_data = []

    for vehicle_type in vehicle_types:
        matching_vehicles = [vehicle for vehicle in vehicles
                             if vehicle.vehicle_type == vehicle_type]
        vehicle_data.append([vehicle_type,
                             matching_vehicles,
                             sum([vehicle.weekly_maintenance_cost for vehicle
                                 in matching_vehicles]),
                             sum([vehicle.weekly_support for vehicle
                                 in matching_vehicles])])
   
    context = {'force': force,
               'force_vehicles': vehicle_data,
               'total_maintenance': maintenance_cost,
               'total_support': support}

    return render(request, 'armoury/force_vehicles.html', context)

