
class  parking:
    def __init__(self,n_floors=2,p_floor=20) -> None:
        # n_floors: number of floors
        # p_floor: default number of parking spaces per floor
        self.parkinglot = {}
        self.n_floors = 0
        self.p_floor = p_floor
        self.in_floor = 1
        self.add_floors(n_floors,p_floor)



    def brute_park(self,car_id):
        for floor_name in self.parkinglot:
            for parking_name in self.parkinglot[floor_name]:
                try:
                    self._park(floor_name,parking_name,car_id)
                    return True
                except:
                    pass
        return False
    
    def brute_unpark(self,car_id):
        for floor_name in self.parkinglot:
            for parking_name in self.parkinglot[floor_name]:
                if self.parkinglot[floor_name][parking_name]['occupied'] == car_id:
                    self._unpark(floor_name,parking_name)
                    return True
        return False
    
    



    def add_floors(self,n_floors,p_floor):
        self._reset_floors(self.n_floors,self.p_floor)
        for i in range(self.n_floors+1,self.n_floors+n_floors):
            floor_name = self._number_to_floor(i)
            for j in range(p_floor):
                self.parkinglot[floor_name][floor_name+str(j)] = {
                    'occupied':None,
                    'working':True
                } 
        self.n_floors += n_floors
    
    def remove_floors(self,n_floors):
        self._reset_floors(self.n_floors,self.p_floor)
        for i in range(self.n_floors-n_floors,self.n_floors):
            floor_name = self._number_to_floor(i)
            del self.parkinglot[floor_name]
        self.n_floors -= n_floors
    

    def add_parking(self,floor_name,n_parking):
        self._reset_floors(self.n_floors,self.p_floor)
        n = len(self.parkinglot[floor_name])
        for j in range(n+1,n+n_parking):
            self.parkinglot[floor_name][floor_name+str(j)] = {
                'occupied':None,
                'working':True
            }
    
    def remove_parking(self,floor_name,n_parking):
        self._reset_floors(self.n_floors,self.p_floor)
        n = len(self.parkinglot[floor_name])
        for j in range(n-n_parking,n):
            del self.parkinglot[floor_name][floor_name+str(j)]

    def _reset_floors(self):
        for i in range(self.n_floors):
            floor_name = self._number_to_floor(i)
            self.parkinglot[floor_name] = {}
            for j in range(self.p_floor):
                self.parkinglot[floor_name][floor_name+str(j)] = {
                    'occupied':None,
                    'working':True
                }


    def _park(self,floor_name,parking_name,car_id):
        if self.parkinglot[floor_name][parking_name]['occupied']:
            raise ValueError('Parking space is occupied')
        
        if not self.parkinglot[floor_name][parking_name]['working']:
            raise ValueError('Parking space is not working')
    
        self.parkinglot[floor_name][parking_name]['occupied'] = car_id
        return True
    
    def _unpark(self,floor_name,parking_name):
        if not self.parkinglot[floor_name][parking_name]['occupied']:
            raise ValueError('Parking space is not occupied')
        self.parkinglot[floor_name][parking_name]['occupied'] = None

    def _repair(self,floor_name,parking_name):
        if self.parkinglot[floor_name][parking_name]['occupied']:
            raise ValueError('Parking space is occupied')
        self.parkinglot[floor_name][parking_name]['working'] = True
    
    def _damage(self,floor_name,parking_name):
        if self.parkinglot[floor_name][parking_name]['occupied']:
            raise ValueError('Parking space is occupied')
        self.parkinglot[floor_name][parking_name]['working'] = False

    def _number_to_floor(number):
        column_name = ''
        while number > 0:
            remainder = (number - 1) % 26
            column_name = chr(65 + remainder) + column_name
            number = (number - 1) // 26
        return column_name
    