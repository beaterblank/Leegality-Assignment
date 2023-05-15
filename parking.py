from typing import Optional

class parking:
    def __init__(self, n_floors:int=2, p_floor:int=20)->None:
        # n_floors: number of floors
        # p_floor: default number of parking spaces per floor
        self.parkinglot = {}  # Dictionary to store parking lot data
        self.n_floors = 0  # Number of floors initialized to 0
        self.p_floor = p_floor  # Default number of parking spaces per floor
        self.in_floor = 1  # Variable to track the current floor
        self.add_floors(n_floors, p_floor)  # Add initial floors to the parking lot

    def park(self, car_id:str) -> Optional[str]:
        # Method to park a car in the parking lot
        for floor_name in self.parkinglot:
            for parking_name in self.parkinglot[floor_name]:
                try:
                    self._park(floor_name, parking_name, car_id)  # Try to park the car
                    return parking_name  # Return the parking space name if successful
                except:
                    pass
        return None  # Return None if no parking space is available

    def unpark(self, car_id:str)->Optional[str]:
        # Method to unpark a car from the parking lot
        for floor_name in self.parkinglot:
            for parking_name in self.parkinglot[floor_name]:
                if self.parkinglot[floor_name][parking_name]['occupied'] == car_id:
                    self._unpark(floor_name, parking_name)  # Unpark the car
                    return parking_name  # Return the parking space name
        return None  # Return None if the car is not found

    def add_floors(self, n_floors:int, p_floor:int)->None:
        # Method to add floors to the parking lot
        for i in range(self.n_floors + 1, self.n_floors + n_floors + 1):
            floor_name = self.number_to_floor(i)  # Get the floor name based on the floor number
            self.parkinglot[floor_name] = {}  # Initialize an empty dictionary for each floor
            for j in range(p_floor):
                # Add parking spaces to the floor dictionary
                self.parkinglot[floor_name][floor_name + str(j + 1)] = {
                    'occupied': None,  # Occupied status of the parking space
                    'working': True  # Working status of the parking space
                }
        self.n_floors += n_floors  # Update the total number of floors

    def remove_floor(self, n_floor:int)->None:
        # Method to remove a floor from the parking lot
        floor_name = self.number_to_floor(n_floor)  # Get the floor name based on the floor number
        del self.parkinglot[floor_name]  # Remove the floor from the parking lot dictionary
        self.n_floors -= 1  # Decrease the total number of floors

    def add_parking(self, floor_name:int, n_parking:int)->None:
        # Method to add parking spaces to a floor
        n = len(self.parkinglot[floor_name])  # Get the current number of parking spaces on the floor
        for j in range(n + 1, n + n_parking):
            # Add parking spaces to the floor dictionary
            self.parkinglot[floor_name][floor_name + str(j + 1)] = {
                'occupied': None,  # Occupied status of the parking space
                'working': True  # Working status of the parking space
            }

    def remove_parking(self, floor_name:int, n_parking:int)->None:
        # Method to remove parking spaces from a floor
        n = len(self.parkinglot[floor_name])  # Get the current number of parking spaces on the floor
        for j in range(n - n_parking, n):
            del self.parkinglot[floor_name][floor_name + str(j + 1)]  # Remove the parking space from the floor

    def _reset_floors(self)->None:
        # Method to reset all the floors in the parking lot
        for i in range(self.n_floors):
            floor_name = self.number_to_floor(i)  # Get the floor name based on the floor number
            self.parkinglot[floor_name] = {}  # Clear the floor dictionary
            for j in range(self.p_floor):
                # Add parking spaces to the floor dictionary
                self.parkinglot[floor_name][floor_name + str(j + 1)] = {
                    'occupied': None,  # Occupied status of the parking space
                    'working': True  # Working status of the parking space
                }

    def _park(self, floor_name:str, parking_name:str, car_id:str)->None:
        # Internal method to park a car in a specific parking space
        if self.parkinglot[floor_name][parking_name]['occupied']:
            raise ValueError('Parking space is occupied')  # Raise an error if the parking space is already occupied
        
        if not self.parkinglot[floor_name][parking_name]['working']:
            raise ValueError('Parking space is not working')  # Raise an error if the parking space is not working
    
        self.parkinglot[floor_name][parking_name]['occupied'] = car_id  # Occupy the parking space with the car ID

    def _unpark(self, floor_name:str, parking_name:str)->None:
        # Internal method to unpark a car from a specific parking space
        if not self.parkinglot[floor_name][parking_name]['occupied']:
            raise ValueError('Parking space is not occupied')  # Raise an error if the parking space is not occupied
        self.parkinglot[floor_name][parking_name]['occupied'] = None  # Clear the occupied status of the parking space

    def repair(self, floor_name:str, parking_name:str)->None:
        # Method to repair a parking space
        if self.parkinglot[floor_name][parking_name]['occupied']:
            raise ValueError('Parking space is occupied')  # Raise an error if the parking space is occupied
        self.parkinglot[floor_name][parking_name]['working'] = True  # Set the working status of the parking space to True

    def damage(self, floor_name:str, parking_name:str)->None:
        # Method to damage a parking space
        if self.parkinglot[floor_name][parking_name]['occupied']:
            raise ValueError('Parking space is occupied')  # Raise an error if the parking space is occupied
        self.parkinglot[floor_name][parking_name]['working'] = False  # Set the working status of the parking space to False

    def number_to_floor(self, number:int)->str:
        # Method to convert a number to a floor name
        column_name = ''
        while number > 0:
            remainder = (number - 1) % 26
            column_name = chr(65 + remainder) + column_name
            number = (number - 1) // 26
        return column_name
    
    def __str__(self) -> str:
        # Method to print the parking lot
        out = ""
        for floor_name in self.parkinglot:
            out += floor_name + "\n"
            for parking_name in self.parkinglot[floor_name]:
                out += parking_name + ": " + str(self.parkinglot[floor_name][parking_name]['occupied']) + "\n"  
            out += "\n"  
        return out


if __name__ == '__main__':
    p = parking(2,20)
    print("initial parking lot\n")
    print(p)

    p.park("car1")
    p.park("car2")

    print("parking car1 and car2\n")

    print(p)

    p.unpark("car1")
    print("unparking car1\n")
    print(p)
    print("adding 2 floors and 4 parking spaces per floor in them\n")
    p.add_floors(2,4)
    print(p)