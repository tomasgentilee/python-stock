import sys
import connection as conect

sys.path.append('c:\\Users\\Segadmin\\Desktop\\Stock\\my_modules')
sys.path.append('c:\\Users\\Segadmin\\Desktop\\Stock\\models')

import instance_class as instance

def push(obj):
    
    class_instance = instance.create_instance(obj)
    
    conect.save_element(class_instance, obj[1])
        

def delete():
    
    var = input("Ingrese el codigo de barras del equipo que desea eliminar: ")
    found = conect.find_barcode(str(var))
    
    if found: 
        var2 = instance.create_instance(found)
        var_y_or_n = input(f"Seguro que desea eliminar el equipo {var2.brand} {var2.model}? (y/n) ")
        if var_y_or_n == "y": 
            conect.delete(found[1], "barcode", var2.barcode)
        elif var_y_or_n == "n":
            print("Cancelando la eliminiación del registro")
    

def edit():
    var = input("Ingrese el código de barras del equipo que desea editar: ")
    found = conect.find_barcode(str(var))
    
    if found:
        var2 = instance.create_instance(found)
        print(f"¿Qué desea editar del equipo {var2.brand} {var2.model}?")
        var2_dict = vars(var2)
        id_value = var2_dict.get("_Phone__id")
        # Mostrar opciones de edición al usuario
        print("Opciones de edición:")
        for i, (key, value) in enumerate(var2_dict.items(), 1):
            display_key = key.replace(f"_{var2.__class__.__name__.lower()}__", "")
            print(f"{i}. {key}: {value}")
        
        # Obtener la opción de edición del usuario
        option = int(input("Seleccione el número de la opción que desea editar: "))
        if 1 <= option <= len(var2_dict):
            key_to_edit = list(var2_dict.keys())[option - 1]
            current_value = var2_dict[key_to_edit]
            new_value = input(f"Ingrese el nuevo valor para '{key_to_edit}' (valor actual: {current_value}): ")
            setattr(var2, key_to_edit, new_value)  # Actualizar el atributo con el nuevo valor
            
            # Llamar a la función 'conect.edit' con los parámetros necesarios
            conect.edit(table_name=found[1], param=display_key, id=id_value, new_value=new_value)
            print(f"El valor de '{key_to_edit}' ha sido actualizado correctamente.")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    else:
        print("Equipo no encontrado. Por favor, verifique el código de barras ingresado.")
       
if __name__ == "__main__":
    
    edit()