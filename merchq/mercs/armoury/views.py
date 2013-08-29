# -*- coding: utf-8 -*-

#   Copyright 2013 Tuukka Turto
#
#   This file is part of unexpected-raptor.
#
#   unexpected-raptor is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   unexpected-raptor is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with unexpected-raptor.  If not, see <http://www.gnu.org/licenses/>.

from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import render, get_object_or_404

from mercs.forces.models import Force
from mercs.armoury.models import VehicleType, Vehicle, WeightClass

from mercs.armoury import process

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

def vehicle_details(request, vehicle_id):

    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    weight_classes = WeightClass.objects.filter(vehicle_type = vehicle.vehicle_type,
                                                lower_limit__lte = vehicle.vehicle_weight,
                                                upper_limit__gte = vehicle.vehicle_weight)

    if weight_classes:
        weight_class = weight_classes[0]
    else:
        weight_class = None

    context = {'vehicle': vehicle,
               'weight_class': weight_class}

    return render(request, 'armoury/vehicle_details.html', context)

def sell_vehicle(request, vehicle_id, confirmed = None):

    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    rating = vehicle.quality_rating
    price = int(vehicle.base_price * 0.5 * rating.cost_modifier)

    if confirmed:       
        process.sell_vehicle(vehicle, price)

    context = {'vehicle': vehicle,
               'price': price,
               'confirmed': confirmed}

    return render(request, 'armoury/sell_vehicle.html', context)

