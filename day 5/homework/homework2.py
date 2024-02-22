import time

# Define the activities of the daily routine
routine_activities = [
    "Wake up",
    "Brush teeth",
    "Breakfast",
    "Go to school",
    "Come back home",
    "Go to maths class",
    "Come back home",
    "Go to dance practise",
    "Come back home",
    "Study programming"
]

# Define the duration (in minutes) for each activity
activity_durations = {
    "Wake up": 5,
    "Brush teeth": 2,
    "Breakfast": 5,
    "Go to school": 10,
    "School stuff": 500,
    "Come back home": 10,
    "Go to maths class": 5,
    "Math stuff": 60,
    "Come back home": 5,
    "Go to dance practise": 10,
    "Dance stuff": 120,
    "Come back home": 10,
    "Study programming": 60
}

# Define the number of repetitions for the daily routine cycle
num_cycles = 3

# Simulate the daily routine cycle
for cycle in range(num_cycles):
    print(f"Cycle {cycle + 1}:")
    for activity in routine_activities:
        duration = activity_durations[activity]
        print(f"{activity}: {duration} minutes")
        time.sleep(duration * 60)  # Convert minutes to seconds
        print(f"Completed {activity}")
    print("\n")
