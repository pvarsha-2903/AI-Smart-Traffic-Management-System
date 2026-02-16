# Fairness-Based Traffic Signal System
# Version 1.2

# Each lane has vehicles and wait time
lanes = {
    "North": {"vehicles": 50, "wait_time": 30},
    "South": {"vehicles": 20, "wait_time": 80},
    "East": {"vehicles": 70, "wait_time": 20},
    "West": {"vehicles": 10, "wait_time": 100}
}

print("=== Traffic and Wait Time Status ===\n")

for lane, data in lanes.items():
    print(f"{lane}: {data['vehicles']} vehicles, Wait Time: {data['wait_time']} sec")

# Decision formula includes fairness
# Weight of wait time prevents starvation
priority_lane = max(
    lanes,
    key=lambda lane: lanes[lane]["vehicles"] + (lanes[lane]["wait_time"] * 0.7)
)

print("\n=== Signal Decision with Fairness ===")
print(f"Priority Lane: {priority_lane}")
