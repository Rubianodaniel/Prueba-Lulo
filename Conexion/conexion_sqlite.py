
from operator import index
import sqlite3 as sql
from sqlalchemy import create_engine 


def createDB():
    ''' 
    crateDB:{ 
    args: None,
    funcion: crea la base de datos en sqlite3
    '''
    try:
        conn = sql.connect("db/database_prueba.db")
        conn.commit()
        conn.close()

    except Exception as ex:
        print(ex)

def createTable():
    ''' 
    crateTable:{ 
    args: None,
    funcion: crea una tabla series en la base de datos "database_prueba"
    '''
    conn = sql.connect("db/database_prueba.db")
    cursor = conn.cursor()
    cursor.execute(
        '''
            CREATE TABLE SERIES (
                id integer PRIMARY KEY AUTOINCREMENT not null,
                name varchar(200),
                unique_id integer   

            )        
        '''
    )
    conn.commit()
    conn.close()

def insert(df,tabla):
    ''' 
    insert:{ 
    args: None,
    funcion: inserta los datos del df_embedded
    '''
    engine = create_engine('sqlite:///db/database_prueba.db', echo = False) 
    df = df.applymap(str)
    df.to_sql(tabla, con=engine,  if_exists='append')