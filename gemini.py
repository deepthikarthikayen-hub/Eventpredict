from google import genai

client = genai.Client(
    api_key="_API_KEY"
)


def generate_suggestions(
    event_type,
    day_of_week,
    venue_capacity,
    current_registrations,
    promotion_budget,
    days_before_event,
    event_duration_hours,
    previous_similar_event_attendance,
    available_organizers,
    total_event_budget,
    prediction,
):

    prompt = f"""
You are an event management assistant.

Event Type: {event_type}
Day of Week: {day_of_week}
Venue Capacity: {venue_capacity}
Current Registrations: {current_registrations}
Promotion Budget: {promotion_budget}
Days Before Event: {days_before_event}
Event Duration: {event_duration_hours} hours
Previous Similar Attendance: {previous_similar_event_attendance}
Available Organizers: {available_organizers}
Total Event Budget: {total_event_budget}

Predicted Attendance: {int(prediction)}

Based on the event details above, generate recommendations that are SPECIFIC to this event.

The suggestions must change depending on:
- Event Type
- Promotion Budget
- Total Event Budget
- Days Before Event
- Venue Capacity
- Current Registrations
- Predicted Attendance
- Available Organizers

Do NOT give generic advice.

If it is a Hackathon, give hackathon-specific ideas.
If it is a College Fest, give college-fest-specific ideas.
If it is a Seminar, give seminar-specific ideas.
If it is a Workshop, give workshop-specific ideas.

Event Readiness Summary:
...

Seating Recommendation:
...

Registration Desk:
...

Volunteer Allocation:
...

Refreshment Estimate:
...

Key Risks:
1.
2.
3.

Immediate Actions:
1.
2.
3.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text