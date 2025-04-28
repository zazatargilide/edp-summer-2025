from enum import Enum

# Event channels
security_channel = []
cage_quality_channel = []
animal_condition_channel = []
general_channel = []

# Enums for better clarity
class SensorType(Enum):
    HUMIDITY = 'humidity'
    TEMPERATURE = 'temperature'
    MOTION = 'motion'

class EventType(Enum):
    ANIMAL_ESCAPE = 'animal_escape'
    TEMPERATURE_ALERT = 'temperature_alert'
    HUMIDITY_ALERT = 'humidity_alert'
    CAGE_CLEANING_NEEDED = 'cage_cleaning_needed'
    ANIMAL_SICK = 'animal_sick'

class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

    def __repr__(self):
        return f"Event(name={self.name}, payload={self.payload})"

class Sensor:
    def __init__(self, id_number, sensor_type: SensorType, cage):
        self.id_number = id_number
        self.sensor_type = sensor_type
        self.cage = cage

    def emit_event(self, name: EventType, payload):
        event = Event(name, payload)
        # Direct to appropriate channel
        if name == EventType.ANIMAL_ESCAPE:
            security_channel.append(event)
        elif name in [EventType.HUMIDITY_ALERT, EventType.TEMPERATURE_ALERT, EventType.CAGE_CLEANING_NEEDED]:
            cage_quality_channel.append(event)
        elif name == EventType.ANIMAL_SICK:
            animal_condition_channel.append(event)
        else:
            general_channel.append(event)
        print(f"[Sensor] Emitted {event} to appropriate channel.")

# Base Employee class
class Employee:
    def __init__(self, id_number, name, role):
        self.id_number = id_number 
        self.name = name
        self.role = role

# Specialized roles
class Vet(Employee):
    def treat_the_animal(self):
        print(f"[Vet {self.name}] Treating the animal")

    def report_to_manager(self):
        print(f"[Vet {self.name}] Sending a report")

    def order_the_medication(self):
        print(f"[Vet {self.name}] I need more medication")

class Guard(Employee):
    def catch_the_animal(self):
        print(f"[Guard {self.name}] I am catching the animal")

    def check_the_cage(self):
        print(f"[Guard {self.name}] I am checking the cage")

    def report_to_manager(self):
        print(f"[Guard {self.name}] I am sending a report")

class Cleaner(Employee):
    def clean_the_cage(self):
        print(f"[Cleaner {self.name}] I am cleaning")

class Zookeeper(Employee):
    def feed_animals(self):
        print(f"[Zookeeper {self.name}] Feeding the animals")

# Event Dispatcher (simple simulation)
def dispatch_events():
    print("\n--- Dispatching Events ---")
    while security_channel:
        event = security_channel.pop(0)
        print(f"[Dispatch] Security Event: {event}")
        guard1.catch_the_animal()
        guard1.report_to_manager()

    while cage_quality_channel:
        event = cage_quality_channel.pop(0)
        print(f"[Dispatch] Cage Quality Event: {event}")
        cleaner1.clean_the_cage()

    while animal_condition_channel:
        event = animal_condition_channel.pop(0)
        print(f"[Dispatch] Animal Condition Event: {event}")
        vet1.treat_the_animal()
        vet1.report_to_manager()

# Creating Employees
zookeeper1 = Zookeeper(1, 'Piotr', 'zookeeper')
cleaner1 = Cleaner(2, 'Kraiven', 'cleaner')
guard1 = Guard(3, 'John', 'guard')
vet1 = Vet(4, 'Mable', 'vet')
manager1 = Employee(5, 'Jane', 'manager')

# Creating Sensors
humidity_sensor1 = Sensor(1, SensorType.HUMIDITY, 'elephants 1')
temperature_sensor1 = Sensor(2, SensorType.TEMPERATURE, 'tigers 1')
motion_sensor1 = Sensor(3, SensorType.MOTION, 'elephants 1')

# Simulate events
humidity_sensor1.emit_event(EventType.HUMIDITY_ALERT, {'value': 85, 'cage': 'elephants 1'})
temperature_sensor1.emit_event(EventType.TEMPERATURE_ALERT, {'value': 40, 'cage': 'tigers 1'})
motion_sensor1.emit_event(EventType.ANIMAL_ESCAPE, {'cage': 'elephants 1'})

# Process events
dispatch_events()
