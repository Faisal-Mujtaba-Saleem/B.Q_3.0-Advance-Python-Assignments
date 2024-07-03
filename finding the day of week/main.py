from datetime import datetime


def find_day_of_week(daystr: str) -> str:
    year, month, day = daystr.split('-')
    if month.startswith('0'):
        month = month[1:len(month)]

    year = int(year)
    month = int(month)
    day = int(day)

    date_object = datetime(year=year, month=month, day=day)
    week_day = date_object.strftime('%A')
    return week_day

# Example Test Cases
# Input: "2024-06-27"
# Output: "Thursday"


day_of_week = find_day_of_week('2024-06-27')
print(day_of_week)

# Input: "2024-01-01"
# Output: "Monday"
day_of_week = find_day_of_week('2024-01-01')
print(day_of_week)
