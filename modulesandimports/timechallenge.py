import pytz
import datetime

available_zones = {
    '1': 'Africa/Tunis',
    '2': 'US/Hawaii',
    '3': 'Europe/Brussels'
}

print("Please choose a timezone or 0 to quit")

for place in sorted(available_zones):
    print(f"{place} {available_zones[place]}")

while True:
    choice = input()

    if choice == '0':
        break
    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        print(tz_to_display, datetime.datetime(available_zones[choice]))
