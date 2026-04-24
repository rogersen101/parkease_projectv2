from datetime import datetime
from django.utils import timezone

def calculate_parking_fee(vehicle):

    now = timezone.now()
    duration_hours = (now - vehicle.arrival_time).total_seconds() / 3600

    current_hour = now.hour

    # Day: 6:00am – 6:59pm
    if 6 <= current_hour <= 18:
        period = 'day'
    else:
        period = 'night'

    vt = vehicle.vehicle_type

    # TRUCK
    if vt == 'truck':
        if duration_hours < 3:
            return 2000
        return 5000 if period == 'day' else 10000

    # PERSONAL CAR
    elif vt == 'car':
        if duration_hours < 3:
            return 2000
        return 3000 if period == 'day' else 2000

    # TAXI
    elif vt == 'taxi':
        if duration_hours < 3:
            return 2000
        return 3000 if period == 'day' else 2000

    # COASTER
    elif vt == 'coaster':
        if duration_hours < 3:
            return 3000
        return 4000 if period == 'day' else 2000

    # BODA-BODA
    elif vt == 'boda':
        if duration_hours < 3:
            return 1000
        return 2000

    return 0