import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='127.0.0.1',           # puede usarse localhost o 127.0.0.1
        user="root",
        password="",                # deja vacío si es XAMPP, NO TIENE CONTRASEÑA.
        database="supermercado",    # va el nombre de la base de datos.
        port=3306                   #es el puerto por defecto de MySQL
    )
    print("Conexión exitosa!")
except mysql.connector.Error as err:
    print("Error:", err)