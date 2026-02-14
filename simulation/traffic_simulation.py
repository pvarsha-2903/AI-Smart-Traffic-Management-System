# Smart Traffic Simulation

lane1 = 50
lane2 = 20
lane3 = 80
lane4 = 10

lanes = {
    "Lane 1": lane1,
    "Lane 2": lane2,
    "Lane 3": lane3,
    "Lane 4": lane4
}

max_lane = max(lanes, key=lanes.get)

print("Traffic Data:")
for lane, cars in lanes.items():
    print(lane, ":", cars, "vehicles")

print("\nPriority Green Signal:", max_lane)
