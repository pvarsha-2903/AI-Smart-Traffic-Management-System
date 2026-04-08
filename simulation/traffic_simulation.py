import time

# Initial traffic data
lanes = {
    "North": {"vehicles": 50, "wait_time": 30},
    "South": {"vehicles": 20, "wait_time": 80},
    "East": {"vehicles": 70, "wait_time": 20},
    "West": {"vehicles": 10, "wait_time": 100}
}

# Function to calculate priority using fairness logic
def calculate_priority(lanes):
    return max(
        lanes,
        key=lambda lane: lanes[lane]["vehicles"] + (lanes[lane]["wait_time"] * 0.7)
    )

# Function to display traffic visually
def display_traffic(lanes):
    print("\n=== 🚗 Traffic Status ===")
    for lane, data in lanes.items():
        bar = "█" * (data["vehicles"] // 5)
        print(f"{lane}: {bar} ({data['vehicles']} cars, wait {data['wait_time']}s)")

print("=== 🚦 Traffic Signal Simulation Started ===")

# Run simulation for multiple cycles
for cycle in range(5):
    display_traffic(lanes)

    priority_lane = calculate_priority(lanes)

    print(f"\n🚦 GREEN SIGNAL: {priority_lane}")
    print("🔴 RED SIGNAL: Other lanes")

    # Simulate signal duration
    time.sleep(2)

    # Update traffic conditions
    for lane in lanes:
        if lane == priority_lane:
            lanes[lane]["wait_time"] = 0
            lanes[lane]["vehicles"] = max(0, lanes[lane]["vehicles"] - 10)
        else:
            lanes[lane]["wait_time"] += 10
