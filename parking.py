
class  parking:
    def __init__(self,n_floors=2,p_floor=20) -> None:
        # n_floors: number of floors
        # p_floor: default number of parking spaces per floor
        self.parkinglot = {}
        self.n_floors = 0
        self.p_floor = p_floor
        self.in_floor = 1
        self.add_floors(n_floors,p_floor)

    def park(self,car_id):
        for floor_name in self.parkinglot:
            for parking_name in self.parkinglot[floor_name]:
                try:
                    self._park(floor_name,parking_name,car_id)
                    return parking_name
                except:
                    pass
        return None
    
    def unpark(self,car_id):
        for floor_name in self.parkinglot:
            for parking_name in self.parkinglot[floor_name]:
                if self.parkinglot[floor_name][parking_name]['occupied'] == car_id:
                    self._unpark(floor_name,parking_name)
                    return parking_name
        return None
    

    
    def add_floors(self,n_floors,p_floor):
        for i in range(self.n_floors+1,self.n_floors+n_floors+1):
            floor_name = self.number_to_floor(i)
            self.parkinglot[floor_name]={}
            for j in range(p_floor):
                self.parkinglot[floor_name][floor_name+str(j+1)] = {
                    'occupied':None,
                    'working':True
                } 
        self.n_floors += n_floors
    
    def remove_floor(self,n_floor):
        floor_name = self.number_to_floor(n_floor)
        del self.parkinglot[floor_name]
        self.n_floors -= 1
    

    def add_parking(self,floor_name,n_parking):
        n = len(self.parkinglot[floor_name])
        for j in range(n+1,n+n_parking):
            self.parkinglot[floor_name][floor_name+str(j+1)] = {
                'occupied':None,
                'working':True
            }
    
    def remove_parking(self,floor_name,n_parking):
        n = len(self.parkinglot[floor_name])
        for j in range(n-n_parking,n):
            del self.parkinglot[floor_name][floor_name+str(j+1)]

    def _reset_floors(self):
        for i in range(self.n_floors):
            floor_name = self.number_to_floor(i)
            self.parkinglot[floor_name] = {}
            self.parkinglot[floor_name]={}
            for j in range(self.p_floor):
                self.parkinglot[floor_name][floor_name+str(j+1)] = {
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

    def repair(self,floor_name,parking_name):
        if self.parkinglot[floor_name][parking_name]['occupied']:
            raise ValueError('Parking space is occupied')
        self.parkinglot[floor_name][parking_name]['working'] = True
    
    def damage(self,floor_name,parking_name):
        if self.parkinglot[floor_name][parking_name]['occupied']:
            raise ValueError('Parking space is occupied')
        self.parkinglot[floor_name][parking_name]['working'] = False

    def number_to_floor(self,number):
        column_name = ''
        while number > 0:
            remainder = (number - 1) % 26
            column_name = chr(65 + remainder) + column_name
            number = (number - 1) // 26
        return column_name
    
    def __str__(self) -> str:
        out = ""
        for floor_name in self.parkinglot:
            out += floor_name + "\n"
            for parking_name in self.parkinglot[floor_name]:
                out += parking_name + ": " + str(self.parkinglot[floor_name][parking_name]['occupied']) + "\n"  
            out += "\n"  
        return out