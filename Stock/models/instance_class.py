import importlib
import inflect
import datetime

def create_instance(t):
    if isinstance(t, tuple) and len(t) >= 2:  # Verificar que t sea una tupla y tenga al menos 2 elementos
        class_name = str(t[1]).capitalize()
        engine = inflect.engine()
        singular_class_name = engine.singular_noun(class_name) or class_name
        module = importlib.import_module(f'{singular_class_name}')
        cls = getattr(module, singular_class_name, None)  # Obtener la clase o None si no se encuentra
        if cls and callable(cls):  # Verificar que cls sea una clase y se pueda llamar
            instance = cls(t[0])
            return instance
        else:
            print(f"Error: No se encontró la clase {class_name} en el módulo {singular_class_name}")
            return None
    else:
        print("Error: La entrada no es una tupla válida para crear una instancia")
        return None

    

if __name__ == "__main__":
    
    t = ((3, 'Glass', '', '8671460385130', 'Samsung', '222chip', datetime.datetime(2024, 3, 22, 12, 48, 32), '', None, 0, 1, 1, '12323213', 'A51', '11671919281', 'phones'), 'phones')
    
    create_instance(t)