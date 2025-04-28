# 📦 1. Working with Classes & Objects
# https://www.w3schools.com/python/python_classes.asp

class Sensor:
    def __init__(self, id_number, sensor_type, cage):
        self.id_number = id_number
        self.sensor_type = sensor_type
        self.cage = cage

    def describe(self):
        print(f"Sensor {self.id_number}: type={self.sensor_type}, cage={self.cage}")

# Task: Create and describe 3 sensors
sensor1 = Sensor(1, 'humidity', 'elephants 1')
sensor2 = Sensor(2, 'temperature', 'tigers 1')
sensor3 = Sensor(3, 'motion', 'elephants 2')

sensors = [sensor1, sensor2, sensor3]

for sensor in sensors:
    sensor.describe()

# 🧰 2. Lists and Object Storage
# https://www.w3schools.com/python/python_lists.asp

class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

events = [
    Event('temperature_alert', {'value': 39}),
    Event('motion_detected', {'location': 'tiger cage'}),
    Event('humidity_low', {'value': 10})
]

# Print all event names
for event in events:
    print(event.name)

# Task: Filter only 'temperature_alert' events
for event in events:
    if event.name == 'temperature_alert':
        print(f"⚠️ Temp Alert: {event.payload}")

# 🔁 3. Loops
# https://www.w3schools.com/python/python_for_loops.asp

employees = ["Piotr", "Jane", "Mable", "John", "Tom"]

# Task: Print a welcome message for each employee
for employee in employees:
    print(f"Welcome {employee}!")

# 🔎 4. Conditionals
# https://www.w3schools.com/python/python_conditions.asp

event_type = "motion_detected"

if event_type == "temperature_alert":
    print("Dispatching vet...")
elif event_type == "motion_detected":
    print("Dispatching guard...")
else:
    print("Unknown event type.")

# 🔎 4. Conditionals
# https://www.w3schools.com/python/python_conditions.asp

event_type = "motion_detected"

if event_type == "temperature_alert":
    print("Dispatching vet...")
elif event_type == "motion_detected":
    print("Dispatching guard...")
else:
    print("Unknown event type.")

# 🧪 6. Functions
# https://www.w3schools.com/python/python_functions.asp

def create_event(name, payload):
    return Event(name, payload)

def handle_event(event):
    print(f"Handling {event.name}: {event.payload}")

e = create_event("humidity_low", {"value": 20})
handle_event(e)

# 🧾 7. Enums and Constants (optional)
# https://docs.python.org/3/library/enum.html

from enum import Enum

class SensorType(Enum):
    HUMIDITY = "humidity"
    TEMPERATURE = "temperature"
    MOTION = "motion"

print(SensorType.HUMIDITY)

# 📄 8. Dictionaries (optional)
# https://www.w3schools.com/python/python_dictionaries.asp

event_handlers = {
    "temperature_alert": "Vet",
    "motion_detected": "Guard",
    "dirty_cage": "Cleaner"
}

# Task: Get responsible role for a given event
event = "motion_detected"
handler = event_handlers.get(event, "Unknown")
print(f"{event} should be handled by {handler}")
