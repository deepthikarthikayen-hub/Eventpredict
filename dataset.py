import pandas as pd
import numpy as np
import random


#creation of list for columns
event_types = [
    "Workshop",
    "Seminar",
    "Hackathon",
    "College Fest",
    "Cultural Event",
    "Corporate Event"
]

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
data = []

for i in range(200):

    event_type = random.choice(event_types)
    day = random.choice(days)

    venue_capacity = random.randint(100, 1000)

    current_registrations = random.randint(
        int(venue_capacity * 0.3),
        int(venue_capacity * 0.9)
    )

    promotion_budget = random.randint(10000, 200000)

    days_before_event = random.randint(1, 60)

    event_duration_hours = random.randint(1, 8)

    previous_similar_event_attendance = random.randint(50, 950)

    available_organizers = random.randint(2, 30)

    total_event_budget = random.randint(20000, 500000)

    actual_attendance = int(
        current_registrations * 0.7
        + previous_similar_event_attendance * 0.3
        + random.randint(-20, 20)
    )

    data.append({
        "event_type": event_type,
        "day_of_week": day,
        "venue_capacity": venue_capacity,
        "current_registrations": current_registrations,
        "promotion_budget": promotion_budget,
        "days_before_event": days_before_event,
        "event_duration_hours": event_duration_hours,
        "previous_similar_event_attendance": previous_similar_event_attendance,
        "available_organizers": available_organizers,
        "total_event_budget": total_event_budget,
        "actual_attendance": actual_attendance
    })
    df = pd.DataFrame(data)
    df.to_csv("dataset.csv", index=False)

print(df.head())
#print(df.columns)
print("Dataset created successfully!")
