import barcode
from barcode.writer import ImageWriter
from barcode import writer
import random
import os
import sys

sys.path.append('c:\\Users\\Segadmin\\Desktop\\Stock\\imagenes')


def code_generator_ean13():
    
    random_num = [random.randint(0,9) for i in range(12)]
    random_num_final = "".join(map(str, random_num))  
    return random_num_final
    
def generate_barcode():
    numeros = code_generator_ean13()
    with open("imagenes/"+str(numeros)+".jpeg", "wb") as fichero:
       code = barcode.EAN13(str(numeros)).get_fullcode()
       barcode.EAN13(code,writer=ImageWriter()).write(fichero)
    
    #printcode(numeros)
    
    return code

def printcode(numeros):
    
    os.startfile("C:/Users/Segadmin/Desktop/Stock/imagenes/"+str(numeros)+".jpeg", "print")