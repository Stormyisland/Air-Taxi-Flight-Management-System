
"""
AIR TAXI FLIGHT MANAGEMENT SYSTEM
---------------------------------
Prototype:
- Flight plan generation
- GPS waypoint generation
- Estimated arrival times
- Multi-aircraft conflict detection
- Advisory collision warnings

NOT CERTIFIED FOR REAL-WORLD FLIGHT OPERATIONS.
"""

import json
import math
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta, timezone
from itertools import combinations


# -------------------------------
# CONFIGURATION
# -------------------------------

EARTH_RADIUS = 6371000  # meters

MIN_HORIZONTAL_SEPARATION = 500.0  # meters (demo setting)
MIN_VERTICAL_SEPARATION = 60.0     # meters (demo setting)

TIME_STEP = 2                       # seconds
WAYPOINT_SPACING = 500              # meters


# -------------------------------
# DATA MODELS
# -------------------------------

@dataclass
class Flight:
    aircraft_id: str
    origin_lat: float
    origin_lon: float
    destination_lat: float
    destination_lon: float
    departure_time: str
    cruise_altitude: float
    speed: float  # meters per second


# -------------------------------
# GEOLOCATION
# -------------------------------

def haversine(lat1, lon1, lat2, lon2):
    """Calculate great-circle distance in meters."""

    lat1, lon1, lat2, lon2 = map(
        math.radians, [lat1, lon1, lat2, lon2]
    )

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    return 2 * EARTH_RADIUS * math.asin(
        math.sqrt(a)
    )

def interpolate_position(lat1, lon1, lat2, lon2, fraction):

     phi1, lam1 = math.radians(lat1), math.radians(lon1)
    phi2, lam2 = math.radians(lat2), math.radians(lon2)

    delta = 2 * math.asin(math.sqrt(
        math.sin((phi2 - phi1) / 2) ** 2
        + math.cos(phi1) * math.cos(phi2)
        * math.sin((lam2 - lam1) / 2) ** 2
    ))

    if delta < 1e-10:
        return lat1, lon1

   a = math.sin((1 - fraction) * delta) / math.sin(delta)
    b = math.sin(fraction * delta) / math.sin(delta)

   x = (
        a * math.cos(phi1) * math.cos(lam1)
        + b * math.cos(phi2) * math.cos(lam2)
    )





