import sys
import datetime

sys.path.append('c:\\Users\\Segadmin\\Desktop\\Stock\\my_modules')
import connection
import barcode_generator as barcode

sys.path.append('c:\\Users\\Segadmin\\Desktop\\Stock\\Enums')
import TableName as TB

import Barcode_Search

class Computer():
    
    def __init__(self, 
                 computer: tuple = None, brand: str = None, model: str = None, ram: str = None, 
                 processor: str = None, solid_disk: str = None, os: str = None, 
                 office: str = None, is_new: bool = None,
                 serial_number: str = None, description: str = None, 
                 table_name: TB = None, asign_date: datetime.datetime = None):
        
        if isinstance(computer, tuple) and computer is not None and len(computer) > 0:
            self.__id = computer[0]
            self.__brand = computer[3]
            self.__model = computer[8]
            self.__barcode = computer[2]
            self.__ram = computer[12]
            self.__processor = computer[11]
            self.__solid_disk = computer[14]
            self.__os = computer[10]
            self.__office = computer[9]
            self.__is_new = computer[7]
            self.__serial_number = computer[13]
            self.__description = computer[5]
            self.__table_name = computer[15]
            self.__employee_id = computer[6]
            self.__date_of_entry = computer[4]
            self.__asign_date = computer[1]
        else:
            self.__brand = brand
            self.__model = model
            self.__barcode = barcode.generate_barcode()
            self.__ram = ram
            self.__processor = processor
            self.__solid_disk = solid_disk
            self.__os = os
            self.__office = office
            self.__is_new = is_new
            self.__serial_number = serial_number
            self.__description = description
            self.__table_name = table_name.value
            self.__employee_id = None
            self.__date_of_entry = datetime.datetime.now()
            self.__asign_date = asign_date
    
    @property 
    def asign_date(self):
        return self.__asign_date
    
    @asign_date.setter 
    def asign_date(self):
        self.__asign_date = datetime.datetime.now()
    
    @property 
    def date_of_entry(self):
        return self.__date_of_entry
      
    @property 
    def brand(self):
        return self.__brand
    
    @brand.setter 
    def brand(self, value):
        self.__brand = value
    
    @property 
    def barcode(self):
        return self.__barcode
    
    @property 
    def model(self):
        return self.__model
    
    @model.setter 
    def brand(self, value):
        self.__model = value
    
    @property    
    def table_name(self):
        return str(self.__table_name)
    
    @property 
    def description(self):
        return self.__description
    
    @description.setter 
    def brand(self, value):
        self.__description = value
    
    @property 
    def serial_number(self):
        return self.__serial_number
    
    @property 
    def is_new(self):
        return self.__is_new
    
    @is_new.setter 
    def is_new(self, value):
        self.__is_new = value
    
    @property 
    def office(self):
        return self.__office
    
    @office.setter 
    def office(self, value):
        self.__office = value
    
    @property 
    def os(self):
        return self.__os
    
    @os.setter 
    def os(self, value):
        self.__os = value
    
    @property 
    def solid_disk(self):
        return self.__solid_disk
    
    @solid_disk.setter 
    def solid_disk(self, value):
        self.__solid_disk = value
    
    @property 
    def processor(self):
        return self.__processor
    
    @processor.setter 
    def processor(self, value):
        self.__processor = value
    
    @property 
    def ram(self):
        return self.__ram
    
    @ram.setter 
    def ram(self, value):
        self.__ram = value
    
    @property 
    def employee_id(self):
        return self.__employee_id
    
    @employee_id.setter 
    def employee_id(self, value):
        self.__employee_id = value
        
        
if __name__ == "__main__":
    # Crear una instancia de la clase BarcodePrueba
    c1 = Computer("()","Lenovo", "ThinkPad", "4GB", "i7", "300GB", "Linux", "10", 0, "T490", "Computadora usada",table_name=TB.TableName.computer, asign_date="")
    
    connection.create_table_foreign_key("computers", c1, "employee")

    # Imprimir el valor inicial del código de barras

    connection.save_element("computers", c1)
    
    c2 = Barcode_Search.BarcodeSearch(c1.table_name, c1.barcode)
           
    connection.save_element("barcode_search", c2)
