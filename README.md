# Leegality-Assignment

Check out.txt to check out test case outputs


The parking class provides a basic implementation of a parking lot management system. It allows cars to be parked and unparked, floors and parking spaces to be added or removed, and the status of the parking lot to be displayed. Additional functionality such as tracking the availability of parking spaces, implementing different parking policies, or integrating with a database can be added based on specific requirements.


## Parking Lot Management System

This code implements a parking lot management system using a Python class called `parking`. The `parking` class represents a parking lot with multiple floors and parking spaces. It provides functionalities to park and unpark cars, add and remove floors and parking spaces, repair and damage parking spaces, and display the current status of the parking lot.

### Class Initialization

```python
parking(n_floors=2, p_floor=20)
```

The `parking` class constructor initializes the parking lot with the specified number of floors (`n_floors`) and the default number of parking spaces per floor (`p_floor`). If the number of floors and parking spaces per floor are not specified, the constructor uses default values of 2 floors and 20 parking spaces per floor. The parking lot is represented as a dictionary called `parkinglot`, where each key represents a floor and contains a dictionary of parking spaces on that floor.

### Functionalities

#### Park

```python
park(car_id)
```

The `park` method is used to park a car in the parking lot. It takes a `car_id` as input and returns the name of the parking space where the car is parked. It iterates through each floor and parking space in the parking lot and checks if the space is available and working. If a suitable parking space is found, the car is parked there, and the name of the parking space is returned. If no available space is found, it returns `None`.

#### Unpark

```python
unpark(car_id)
```

The `unpark` method is used to unpark a car from the parking lot. It takes a `car_id` as input and searches for the parking space where the car is parked. If the car is found, it removes the car from the parking space and returns the name of the parking space. If the car is not found, it returns `None`.

#### Add Floors

```python
add_floors(n_floors, p_floor)
```

The `add_floors` method is used to add new floors to the parking lot. It takes the number of floors (`n_floors`) and the number of parking spaces per floor (`p_floor`) as input. It creates new floor entries in the `parkinglot` dictionary and adds the specified number of parking spaces on each floor.

#### Remove Floor

```python
remove_floor(n_floor)
```

The `remove_floor` method is used to remove a floor from the parking lot. It takes the floor number (`n_floor`) as input and removes the corresponding floor entry from the `parkinglot` dictionary.

#### Add Parking

```python
add_parking(floor_name, n_parking)
```

The `add_parking` method is used to add new parking spaces to a specific floor. It takes the floor name (`floor_name`) and the number of parking spaces to add (`n_parking`) as input. It creates new parking space entries on the specified floor in the `parkinglot` dictionary.

#### Remove Parking

```python
remove_parking(floor_name, n_parking)
```

The `remove_parking` method is used to remove parking spaces from a specific floor. It takes the floor name (`floor_name`) and the number of parking spaces to remove (`n_parking`) as input. It removes the specified number of parking space entries from the `parkinglot` dictionary.

#### Repair

```python
repair(floor_name, parking_name)
```

The `repair` method is used to mark a parking space as working. It takes the floor name (`floor_name`) and the parking space name (`parking_name`) as input. It sets the `working` attribute of the specified parking space in the `parkinglot` dictionary to `True`, indicating that the parking space is in working condition. This method can be used after a parking space has been damaged and repaired.

#### Damage

```python
damage(floor_name, parking_name)
```

The `damage` method is used to mark a parking space as damaged. It takes the floor name (`floor_name`) and the parking space name (`parking_name`) as input. It sets the `working` attribute of the specified parking space in the `parkinglot` dictionary to `False`, indicating that the parking space is not in working condition. This method can be used to simulate a parking space being out of order.

#### Number to Floor

```python
number_to_floor(number)
```

The `number_to_floor` method is a helper method used to convert a numeric floor number to an alphabetic representation. It takes a numeric floor number as input and returns the corresponding alphabetic representation. For example, floor number 1 is converted to 'A', floor number 2 is converted to 'B', and so on.

#### Display

```python
__str__()
```

The `__str__` method is overridden to provide a string representation of the current status of the parking lot. It returns a formatted string that displays each floor and the occupied status of each parking space on that floor.