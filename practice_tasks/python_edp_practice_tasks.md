
# 🧠 Python Practice Tasks – Foundation for Event-Driven Systems

This list includes the key Python concepts your students should practice before building an event-driven zoo monitoring system. Each section contains task ideas and a helpful W3Schools link.

---

## 1️⃣ Variables & Data Types
**Task Ideas:**
- Create variables for sensor ID, type, and location.
- Store animal names, cage numbers, and temperatures.

🔗 [Python Variables](https://www.w3schools.com/python/python_variables.asp)  
🔗 [Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)

---

## 2️⃣ Strings & String Methods
**Task Ideas:**
- Combine strings to make log messages (e.g., `"Sensor " + sensor_id + " active"`).
- Format strings with `f"{}"` to display event info.

🔗 [Python Strings](https://www.w3schools.com/python/python_strings.asp)  
🔗 [Python String Methods](https://www.w3schools.com/python/python_strings_methods.asp)

---

## 3️⃣ Lists
**Task Ideas:**
- Store a list of sensors or employees.
- Iterate over the list and print each item.

🔗 [Python Lists](https://www.w3schools.com/python/python_lists.asp)

---

## 4️⃣ Dictionaries
**Task Ideas:**
- Create a dictionary to map event types to employees (`{"motion_detected": "Guard"}`).
- Use `.get()` to safely retrieve values.

🔗 [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)

---

## 5️⃣ Conditionals (`if`, `elif`, `else`)
**Task Ideas:**
- Check event type and print who should handle it.
- If temperature is too high, print a warning.

🔗 [Python Conditions](https://www.w3schools.com/python/python_conditions.asp)

---

## 6️⃣ Loops (`for`, `while`)
**Task Ideas:**
- Use a loop to check multiple sensors or process events.
- Count the number of events per type.

🔗 [Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)  
🔗 [Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)

---

## 7️⃣ Functions
**Task Ideas:**
- Write a function `create_event()` that returns a dictionary with `name` and `payload`.
- Write a function `handle_event()` that prints event information.

🔗 [Python Functions](https://www.w3schools.com/python/python_functions.asp)

---

## 8️⃣ Classes & Objects
**Task Ideas:**
- Create a `Sensor` class with an `emit_event()` method.
- Create an `Employee` class with subclasses like `Vet`, `Guard`.

🔗 [Python Classes and Objects](https://www.w3schools.com/python/python_classes.asp)

---

## 9️⃣ Inheritance
**Task Ideas:**
- Inherit `Employee` class and override methods for different roles.
- Use `super().__init__()` to initialize base class attributes.

🔗 [Python Inheritance](https://www.w3schools.com/python/python_inheritance.asp)

---

## 🔟 Modules and Importing
**Task Ideas:**
- Create a file `sensor.py` with the `Sensor` class and import it.
- Practice organizing code into multiple files.

🔗 [Python Modules](https://www.w3schools.com/python/python_modules.asp)

---

## 🔁 Bonus: Enum (Advanced Stretch)
**Task Ideas:**
- Define an `Enum` for `SensorType` or `EventType`.

🔗 [Python Enum Reference](https://www.w3schools.com/python/ref_enum.asp)
