from car import Car

my_car = Car('Ferrari', 2020, 'Red', True)
print(my_car.model)
print(my_car.color)
print(my_car.year)
print(my_car.for_sale)

my_car.drive()
my_car.stop()
my_car.describe()

new_car = Car('BMW', 2021, 'Blue', False)
print(new_car.model)
print(new_car.color)
print(new_car.year)
print(new_car.for_sale)

new_car.drive()
new_car.stop()
new_car.describe()