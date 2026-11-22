
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





