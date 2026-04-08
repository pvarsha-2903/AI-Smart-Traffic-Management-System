import time

# Initial traffic data
lanes = {
    "North": {"vehicles": 50, "wait_time": 30},
    "South": {"vehicles": 20, "wait_time": 80},
    "East": {"vehicles": 70, "wait_time": 20},
    "West": {"vehicles": 10, "wait_time": 100}
}

# Fairness-based priority function
def calculate_priority(lanes):
    return max(
        lanes,
        key=lambda lane: lanes[lane]["vehicles"] + (lanes[lane]["wait_time"] * 0.7)
    )

# Emoji-based traffic display 🚗
def display_traffic(lanes):
    print("\n=== 🚗 Traffic Status ===")
    for lane, data in lanes.items():
        cars = "🚗" * (data["vehicles"] // 10)
        print(f"{lane:6}: {cars} ({data['vehicles']} cars, {data['wait_time']}s wait)")

# Signal display 🚦
def display_signal(lanes, priority_lane):
    print("\n=== 🚦 SIGNAL STATUS ===")
    for lane in lanes:
        if lane == priority_lane:
            print(f"{lane:6}: 🟢 GREEN")
        else:
            print(f"{lane:6}: 🔴 RED")

print("=== 🚦 Traffic Signal Simulation Started ===")

# Run simulation
for cycle in range(5):
    display_traffic(lanes)

    priority_lane = calculate_priority(lanes)

    display_signal(lanes, priority_lane)

    # Simulate signal duration
    time.sleep(2)

    # Update traffic conditions
    for lane in lanes:
        if lane == priority_lane:
            lanes[lane]["wait_time"] = 0
            lanes[lane]["vehicles"] = max(0, lanes[lane]["vehicles"] - 10)
        else:
            lanes[lane]["wait_time"] += 10
