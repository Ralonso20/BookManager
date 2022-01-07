import sqlite3
from sqlite3  import Error
from sqlite3.dbapi2 import threadsafety
from types import TracebackType

#El archivo se encarga de la conexion con la base de datos

def create_conection():
    try:
        conn = sqlite3.connect('db/book_db')
        return conn #si no ocurre ningun error devolvemos la conexion
    except Error as e:
        print("Error connecting to db: " + str(e)) #Si salta el error imprimimos un mensaje concatenando
        #el error establecido como str para concatenar