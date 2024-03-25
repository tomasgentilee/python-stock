import mysql.connector
import type_converter_for_mysql as convert

class MySQLconect:
    
    @staticmethod
    def connector_db():
        
        try:
            connect = mysql.connector.connect(
                host='localhost',
                user='root',
                password='toor',
                database='Stock',
                port='3306'
            )
            
            return connect
        
        except mysql.connector.Error as error:
            
            print("Error al conectar con la base de datos {}".format(error))
            
            return connect
        
def save_element(table_name, obj):
        
        try:
            connect = MySQLconect.connector_db()
            cursor = connect.cursor()

            # Obtener los nombres de los atributos del objeto
            attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__") and not attr.startswith("_")  and not attr.startswith("_Phone__")]
            
            # Obtener los valores de los atributos del objeto
            values = [getattr(obj, attr) for attr in attributes]

            # Crear una cadena de placeholders para la consulta SQL
            placeholders = ",".join(["%s"] * len(attributes))

            # Crear la consulta SQL dinámica para insertar el registro
            instruction = f"INSERT INTO {table_name} ({','.join(attributes)}) VALUES ({placeholders})"
        
            cursor.execute(instruction, values)
        
            connect.commit()
            print("Registro insertado correctamente.")
            
            return 1
            
        except mysql.connector.Error as error:
            
            print("Error al cargar los datos {}".format(error))

def find_element(table_name, param, value):
    
    try:
        connect = MySQLconect.connector_db()
        cursor = connect.cursor()

        # Consulta SQL para seleccionar un producto por su nombre
        query = f"SELECT * FROM {table_name} WHERE {param} = %s"

        # Ejecutar la consulta con el nombre del producto como parámetro
        cursor.execute(query, (value,))

        # Obtener el resultado de la consulta
        result = cursor.fetchone()

        if result:
            return result
        else:
            print("Equipo no encontrado.")

    except mysql.connector.Error as error:
        print("Error al conectar con la base de datos:", error)

    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()          
            
def create_table(table_name, obj):
    try:
        # Establecer conexión a la base de datos
        connect = MySQLconect.connector_db()
        cursor = connect.cursor()

        # Obtener los atributos y tipos de datos del objeto
        attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__") and not attr.startswith("_")]

        columns = [f"{attr} {convert.convert(getattr(obj, attr))}" for attr in attributes]

        for i in range(len(columns)):
            if "None" in columns[i]:
                columns[i] = columns[i].replace("None", "NULL")
            elif f"{table_name}_id None" in columns[i]:
                columns[i] = f"{table_name}_id INT NULL"

        # Crear la consulta SQL para crear la tabla
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({f'{table_name}_id INT PRIMARY KEY AUTO_INCREMENT, ' + ', '.join(columns)})"

        # Ejecutar la consulta SQL
        cursor.execute(create_table_query)

        # Confirmar cambios en la base de datos
        connect.commit()
        print(f"Tabla '{table_name}' creada correctamente.")

    except mysql.connector.Error as error:
        print("Error al conectar con la base de datos:", error)

    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()
                             
def create_table_foreign_key(table_name, obj, foreign_table):
    
    try:
        # Establecer conexión a la base de datos
        connect = MySQLconect.connector_db()
        cursor = connect.cursor()
        
        foreign_key = f"FOREIGN KEY ({foreign_table}_id) REFERENCES {foreign_table}({foreign_table}_id) ON DELETE SET NULL"

        # Obtener los atributos y tipos de datos del objeto
        attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__") and not attr.startswith("_")]

        columns = [f"{attr} {convert.convert(getattr(obj, attr))}" for attr in attributes]

        for i in range(len(columns)):
            columns
            if columns[i] == (f"{foreign_table}_id None"):
                columns[i] = f"{foreign_table}_id INT NULL"
                
        # Crear la consulta SQL para crear la tabla
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({f'{table_name}_id INT PRIMARY KEY AUTO_INCREMENT, ' + ', '.join(columns) + ', ' + foreign_key})"

        # Ejecutar la consulta SQL
        cursor.execute(create_table_query)

        # Confirmar cambios en la base de datos
        connect.commit()
        print(f"Tabla '{table_name}' creada correctamente.")

    except mysql.connector.Error as error:
        print("Error al conectar con la base de datos:", error)

    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()
                     
def insert_many(table_name, values, params):
    
    try:
        connect = MySQLconect.connector_db()
        cursor = connect.cursor()

        sql = f"INSERT INTO {table_name} {params} VALUES (%s, %s)"

        for val in values:
            cursor.execute(sql, val)

        connect.commit()

    except mysql.connector.Error as error:
        print("Error al conectar con la base de datos:", error)

    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()
                     
def find_barcode(value):
    
    try:
        connect = MySQLconect.connector_db()
        cursor = connect.cursor()
        
        barcode = find_element("barcode_search", "barcode", value)
        
        if barcode != None:
            result = find_element(barcode[2], "barcode", barcode[1])
            return (result, str(barcode[2]))
        else:
            print("Equipo no encontrado")

        connect.commit()

    except mysql.connector.Error as error:
        print("Error al conectar con la base de datos:", error)

    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()

def find_the_owner(value):
    
    try:
        connect = MySQLconect.connector_db()
        cursor = connect.cursor()
        
        barcode = find_element("employee", "employee_id", value)

        connect.commit()
        
        return barcode

    except mysql.connector.Error as error:
        print("Error al conectar con la base de datos:", error)

    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()
            
def delete(table_name, param, value):
    
    try:
        connect = MySQLconect.connector_db()
        cursor = connect.cursor()

        # Consulta SQL para seleccionar un producto por su nombre
        query = f"DELETE FROM {table_name} WHERE {param} = {value}"
        cursor.execute(query)
        connect.commit()
        
        if param == "barcode":
            query = f"DELETE FROM barcode_search WHERE {param} = {value}"
            cursor.execute(query)
            connect.commit()
        
        print (f"El dispositivo con codigo de barras {param} se elimino correctamente de la tabla {table_name}")
        
    except mysql.connector.Error as error:
        print("Error al conectar con la base de datos:", error)

    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()       
          
def edit(table_name, param, id, new_value):
    
    try:
        connect = MySQLconect.connector_db()
        cursor = connect.cursor()
        
        query = f"UPDATE {table_name} SET {param} = {new_value} WHERE (`{table_name}_id` = {id});"
        
        cursor.execute(query)
        connect.commit()
        
        
        print("Registro editado correctamente")

    except mysql.connector.Error as error:
        print("Error al conectar con la base de datos:", error)

    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()
          