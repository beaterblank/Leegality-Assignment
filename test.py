from parking import parking

p = parking(2,4)
print(p)

p.park("car1")
p.park("car2")
print(p)
p.unpark("car1")
print(p)
p.add_floors(2,4)
print(p)