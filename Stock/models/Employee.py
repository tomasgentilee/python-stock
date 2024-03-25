import sys
import datetime

sys.path.append('c:\\Users\\Segadmin\\Desktop\\Stock\\my_modules')
import connection

sys.path.append('c:\\Users\\Segadmin\\Desktop\\Stock\\Enums')
import TableName as TB
import WorkArea as WA

class Employee:
    def __init__(self, employee: tuple = None, name: str = None, last_name: str = None, dni: int = None,
                 address: str = None, city: str = None, work_area: WA = None, legajo: int = None):
        
        if isinstance(employee, tuple) and employee is not None and len(employee) > 0:
            # Inicializar desde una tupla
            self.__id = employee[0]
            self.__name = employee[6]
            self.__last_name = employee[4]
            self.__dni = employee[3]
            self.__address = employee[1]
            self.__city = employee[2]
            self.__work_area = employee[8]
            self.__upload_date = employee[7]
            self.__legajo = employee[5]
        else:
            # Inicializar con parámetros individuales
            self.__name = name
            self.__last_name = last_name
            self.__dni = dni
            self.__address = address
            self.__city = city
            self.__work_area = work_area.value
            self.__upload_date = datetime.datetime.now()
            self.__legajo = legajo
    
    @property 
    def legajo(self):
        return self.__legajo
    @legajo.setter 
    def legajo(self):
        self.__legajo = datetime.datetime.now()

    @property 
    def upload_date(self):
        return self.__upload_date
    @upload_date.setter 
    def upload_date(self):
        self.__upload_date = datetime.datetime.now()
        
    @property 
    def name(self):
        return self.__name
    @name.setter 
    def name(self, value):
        self.__name = value
            
    @property 
    def last_name(self):
        return self.__last_name
    @last_name.setter 
    def last_name(self, value):
        self.__last_name = value
            
    @property 
    def dni (self):
        return self.__dni
    @dni.setter 
    def dni(self, value):
        self.__dni = value
            
    @property 
    def address(self):
        return self.__address
    @address.setter 
    def address(self, value):
        self.__address = value 
            
    @property 
    def city (self):
        return self.__city 
    @city.setter 
    def city(self, value):
        self.__city = value
        
    @property 
    def work_area (self):
        return self.__work_area
    @work_area.setter 
    def work_area(self, value):
        self.__work_area = value
            
if __name__ == "__main__":
    
    # Crear una instancia de la clase BarcodePrueba
    e1 = Employee("()","Tomas", "Gentile", 42586769, "Rebizo 539", "Monte Grande", work_area = WA.WorkArea.seguridad_informatica, legajo = 898)

    connection.create_table("employee", e1)

    connection.save_element("employee", e1)
