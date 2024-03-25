import sys
import datetime

sys.path.append('c:\\Users\\Segadmin\\Desktop\\Stock\\my_modules')
import connection
import barcode_generator as barcode

sys.path.append('c:\\Users\\Segadmin\\Desktop\\Stock\\Enums')
import TableName as TB

import Barcode_Search

class Phone:
    def __init__(self, 
                 phone: tuple = None, brand: str = None, model: str = None, imei: str = None, 
                 phone_number: str = None, chip_id: str = None, accesories: str = None, 
                 has_charger: bool = None, has_headphones: bool = None, has_usb: bool = None,
                 table_name: TB = None, description: str = None, 
                 asign_date: datetime.datetime = None):
        
        if isinstance(phone, tuple) and phone is not None and len(phone) > 0:
            # Inicializar desde una tupla
            self.__id = phone[0]
            self.__brand = phone[4]
            self.__model = phone[13]
            self.__imei = phone[12]
            self.__barcode = phone[3]
            self.__phone_number = phone[14]
            self.__chip_id = phone[5]
            self.__has_charger = phone[9]
            self.__has_headphones = phone[10]
            self.__has_usb = phone[11]
            self.__accesories = phone[1]
            self.__table_name = phone[15]
            self.__description = phone[7]
            self.__date_of_entry = phone[6]
            self.__asign_date = phone[2]
            self.__employee_id = phone[8]
            self.__phone_id = phone[0]
        else:
            # Inicializar con parámetros individuales
            self.__brand = brand
            self.__model = model
            self.__imei = imei
            self.__barcode = barcode.generate_barcode()
            self.__phone_number = phone_number
            self.__chip_id = chip_id
            self.__has_charger = has_charger
            self.__has_headphones = has_headphones
            self.__has_usb = has_usb
            self.__accesories = accesories
            self.__table_name = table_name.value
            self.__description = description
            self.__date_of_entry = datetime.datetime.now()
            self.__asign_date = asign_date
            self.__employee_id = None
    
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
    
    @property 
    def barcode(self):
        return self.__barcode
    
    @property 
    def model(self):
        return self.__model
    
    @property    
    def table_name(self):
        return str(self.__table_name)
    
    @property 
    def imei(self):
        return self.__imei
    
    @property 
    def phone_number(self):
        return self.__phone_number
    
    @property 
    def chip_id(self):
        return self.__chip_id
    
    @property 
    def has_charger(self):
        return self.__has_charger
    
    @property 
    def has_headphones(self):
        return self.__has_headphones
    
    @property 
    def has_usb(self):
        return self.__has_usb
    
    @property 
    def accesories(self):
        return self.__accesories
    
    @property 
    def description(self):
        return self.__description
    
    @property 
    def employee_id(self):
        return self.__employee_id
    
    @employee_id.setter 
    def employee_id(self, value):
        self.__employee_id = value
    
    
if __name__ == "__main__":
    
    # Crear una instancia de la clase BarcodePrueba
    p1 = Phone("()","Samsung", "A51", "12323213", "11671919281", "222chip", "Glass", False ,True ,True ,table_name=TB.TableName.phone, description="description", asign_date="")
    
    connection.create_table_foreign_key(p1.table_name, p1, "employee")
    
    connection.save_element(p1.table_name, p1)
    
    p2 = Barcode_Search.BarcodeSearch(p1.table_name, p1.barcode)
    
    connection.save_element("barcode_search", p2)
