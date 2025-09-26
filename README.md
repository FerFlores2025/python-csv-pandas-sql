Este repositorio contiene distintos scripts en *Python* para trabajar con archivos CSV y con una base de datos MySQL.  

## Archivos principales

## Archivos CSV 
- Son los archivos descargados de la Base de Datos : SUPERMERCADO.

## Proyecto.final.py
- Permite *leer archivos CSV de a uno por vez*.  
- Ideal para pruebas rápidas o para trabajar con un dataset en particular.  

## Proyectocombinado.py
- Permite *acceder a cualquier CSV* de forma más flexible.  
- Diseñado para integrar distintos archivos en un mismo flujo de trabajo.
- Te permite insertar, modificar, eliminar datos.

## Conectormysql.py
- Contiene las funciones necesarias para establecer la *conexión con MySQL*.  
- Sirve para enviar datos desde los CSV hacia la base de datos, o para consultar la información ya almacenada.  



## Requisitos
- Python 3.11 o superior  
- Librerías indicadas en requirements.txt (pueden instalarse con:  
  ```bash
  pip install -r requirements.txt
- Para unir Python con SQL primero necesito instalar :
  pip install mysql-connector-python
  
