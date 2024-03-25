import mysql.connector

# Conectar a la base de datos
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='toor',
    database='Stock'
)

# Crear un cursor para ejecutar consultas SQL
my_cursor = db.cursor()

def create_db(db_name):
    # Crear la base de datos
    instruction = f"CREATE DATABASE IF NOT EXISTS {db_name}"
    my_cursor.execute(instruction)
    print(f"Base de datos '{db_name}' creada correctamente.")

def create_table(table_name):
    # Crear una tabla en la base de datos
    instruction = f"""CREATE TABLE IF NOT EXISTS {table_name} (
        barcode_id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50),
        barcode VARCHAR(13)
    )"""
    my_cursor.execute(instruction)
    print(f"Tabla '{table_name}' creada correctamente.")

def describe_table(table_name):
    # Describir la estructura de una tabla
    instruction = f"DESCRIBE {table_name}"
    my_cursor.execute(instruction)
    print(f"Descripción de la tabla '{table_name}':")
    for column in my_cursor:
        print(column)

def insert_element(table_name, name, barcode):
    # Insertar un elemento en la tabla
    instruction = f"INSERT INTO {table_name} (name, barcode) VALUES (%s, %s)"
    values = (name, barcode)
    my_cursor.execute(instruction, values)
    db.commit()
    print("Elemento insertado correctamente.")

def select_from(table_name):
    # Seleccionar todos los elementos de la tabla
    instruction = f"SELECT * FROM {table_name}"
    my_cursor.execute(instruction)
    print(f"Registros en la tabla '{table_name}':")
    for record in my_cursor:
        print(record)
        
def save_record(obj, table_name):
    # Crear una lista de los nombres de los atributos del objeto
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Crear una lista de valores de los atributos del objeto
    values = [getattr(obj, attr) for attr in attributes]

    # Crear una cadena de placeholders para la consulta SQL
    placeholders = ",".join(["%s"] * len(attributes))

    # Crear la consulta SQL dinámica para insertar el registro
    instruction = f"INSERT INTO {table_name} ({','.join(attributes)}) VALUES ({placeholders})"
    my_cursor.execute(instruction, values)
    db.commit()
    print("Registro insertado correctamente.")

if __name__ == "__main__":
    #Crear la base de datos y la tabla si no existen
    create_db("Stock")
    
    create_table("test")

    # Describir la tabla para verificar su estructura
    describe_table("test")

    # Insertar un elemento en la tabla
    insert_element("test", "Producto de prueba", "1234567890123")

    # Seleccionar y mostrar todos los elementos de la tabla
    select_from("test")

    # Cerrar la conexión a la base de datos
    db.close()
    
    # Guardar multiples registros
    save_record("obj", "table_name")