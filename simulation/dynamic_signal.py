# Dynamic Traffic Signal Timing System
# Version 1.1

# Number of vehicles in each lane
lanes = {
    "North": 20,
    "South": 45,
    "East": 80,
    "West": 15
}

print("=== Traffic Status ===\n")

# Display traffic
for lane, vehicles in lanes.items():
    print(f"{lane} Lane: {vehicles} vehicles")

# Select lane with highest traffic
priority_lane = max(lanes, key=lanes.get)

# Calculate green signal time
# Logic: more vehicles = more time
base_time = 10
extra_time_per_vehicle = 0.5

green_time = base_time + (lanes[priority_lane] * extra_time_per_vehicle)

# Apply limits
if green_time > 60:
    green_time = 60
elif green_time < 10:
    green_time = 10

print("\n=== Signal Decision ===")
print(f"Green Signal: {priority_lane} Lane")
print(f"Green Time: {int(green_time)} seconds")
