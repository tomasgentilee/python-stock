import sys

sys.path.append('c:\\Users\\Segadmin\\Desktop\\Stock\\my_modules')

import connection

sys.path.append('c:\\Users\\Segadmin\\Desktop\\Stock\\models')

import Employee
import instance_class as instance_class

var = input("Ingrese el código de barras: ")

devise = connection.find_barcode(str(var))
print(devise)
devise1 = instance_class.create_instance(devise)
print(devise1.employee_id)

print(" ")
print("Datos obtenidos:")
print(" ")

if devise1.employee_id != None and devise1.employee_id != '' and devise1.employee_id:
    person = connection.find_the_owner(devise1.employee_id)
    person1 = Employee.Employee(person)
    print(" ")
    person_dict = vars(person1)
    for key, value in person_dict.items():
            print(f"The {key} is {value}")
    print(" ")  
else:
    pass
    
devise_dict = vars(devise1)
for key, value in devise_dict.items():
    print(f"The {key} is {value}")
print(" ")
print("------------")
print(" ")

print(f"""El equipo {devise1.brand} pertenece a {person1.name} {person1.last_name} de {person1.work_area}""")
