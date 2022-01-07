import sqlite3
from sqlite3 import Error
from .conection import create_conection #con el punto establecemos el mismo path

#En este archivo estan las consultas para la base de datos


def insert_book(data):
    conn = create_conection()
    sql = """ INSERT INTO BOOKS (TITLE, CATEGORY, PAGE_QTY, BOOK_PATH, DESCRIPTION)
                VALUES(?, ?, ?, ?, ?)
    """
    try:
        cur = conn.cursor() #Establecemos el cursor
        cur.execute(sql,data)#Pasamos la consulta y los datos
        conn.commit()#Aplicamos la operacion
        print("New book aggregate")
        return True #avisamos que la insercion fue correcta
    except Error as e:
        print("Error inserting new book: " + str(e))
    finally: #esto siempre se ejecuta independientemente de si ocurre o no un error
        if conn:
            cur.close()
            conn.close() #es buena practica cerrar la conexion despues de la consulta


def update_book(_id,data): #para poder agregar variables a strings colocamos una f
    conn = create_conection()
    sql = f""" UPDATE BOOKS SET 
                            TITLE = ?,
                            CATEGORY = ?,
                            PAGE_QTY = ?,
                            PAGE_QTY_READ = ?,
                            BOOK_PATH = ?,
                            DESCRIPTION = ?
            WHERE BOOK_ID = {_id} 
            
    """

    try:
        cur = conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        print("Edit book succes")
        return True
    except Error as e:
        print("Error updating book: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book(_id):
    conn = create_conection()
    sql = f" DELETE from BOOKS where BOOK_ID = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql) #aca no recive datos, solo la conexion
        conn.commit()
        print("Delete book succes")
        return True
    except Error as e:
        print("Error deleting book: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_books():
    conn = create_conection()
    sql = """ SELECT * FROM BOOKS """

    try:
        cur = conn.cursor()
        cur.execute(sql)
        #En las funciones en las que no agreamos datos no necesitamos hacer un commit
        #Asi que los capturamos de la siguiente manera
        books = cur.fetchall() #traemos todos los datos y los almacenamos
        return books
    except Error as e:
        print("Error selecting  all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_id(_id):
    conn = create_conection()
    sql = f" SELECT * FROM BOOKS WHERE BOOK_ID = {_id} "

    try:
        cur = conn.cursor()
        cur.execute(sql)
        book = cur.fetchone() #la consulta solo retorna un valor
        return book
    except Error as e:
        print("Error selecting book by id: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_title(TITLE):
    conn = create_conection() #Usamos like para la consulta para buscar titulos similares, no exactamemte iguales
    sql = f" SELECT * FROM BOOKS WHERE TITLE LIKE '%{TITLE}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        book = cur.fetchall() #la consulta en este caso puede mostrar muchos libros con los titulos similares
        return book
    except Error as e:
        print("Error selecting book by title: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_category(CATEGORY):
    conn = create_conection()
    sql = f" SELECT * FROM BOOKS WHERE CATEGORY LIKE '%{CATEGORY}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        book = cur.fetchall()
        return book
    except Error as e:
        print("Error selecting book by category: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()



