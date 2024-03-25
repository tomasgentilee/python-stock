def create_table_foreign_key(table_name, obj, foreign_table):
    
    try:
        # Establecer conexión a la base de datos
        connect = MySQLconect.connector_db()
        cursor = connect.cursor()
        
        foreign_key = f"FOREIGN KEY ({foreign_table}_id) REFERENCES {foreign_table}({foreign_table}_id) ON DELETE SET NULL"


        # Obtener los atributos y tipos de datos del objeto
        attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__") and not attr.startswith("_")]

        columns = [f"{attr} {convert.convert(getattr(obj, attr))}" if getattr(obj, attr) is not None else f"{attr} NULL" for attr in attributes]


        # Crear la consulta SQL para crear la tabla
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({f'{table_name}_id INT PRIMARY KEY AUTO_INCREMENT, ' + ', '.join(columns) + ', ' + foreign_key })"

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
            print("Conexión cerrada.")
 