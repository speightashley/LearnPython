vehicles = {'dream': 'Honda 250T', 'roadster': 'BMW R1100', 'er5': 'Kawasaki ER5', 'can-am': 'Bombardier Can-am 250',
            'virago': 'Yamaha XV250', 'tenere': 'Yamaha XT650', 'jimny': 'Suzuki Jimny 1.5',
            'Fiesta': 'Ford Fiesta Ghia 1.4', 'Glider': 'toy'}

my_car = vehicles['Fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)

learner = vehicles.get("er5")
print(learner)

del vehicles["dream"]
# del vehicles["F1"]
result = vehicles.pop("f1", None)
print(result)

plane = vehicles.pop("learjet", "Doesn't exist")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
#  for key in vehicles:
#     print(key, vehicles[key], sep=", ")

for key, value in vehicles.items():
    print(key, value, sep=", ")
