import sys

sys.path.append('c:\\Users\\Segadmin\\Desktop\\Stock\\my_modules')
import connection


class BarcodeSearch:
    
    def __init__(self, table_name: str, barcode: str):    
        self.__barcode = barcode
        self.__table_name = table_name
    
    @property    
    def table_name(self):
        return self.__table_name
    
    @property 
    def barcode(self):
        return self.__barcode
    
    
    
if __name__ == "__main__":
    # Crear una instancia de la clase BarcodePrueba
    c1 = BarcodeSearch("computers", "22222")

    connection.create_table("barcode_search", c1)

    # Imprimir el valor inicial del código de barras

    #connection.save_element("barcode_search", c1)