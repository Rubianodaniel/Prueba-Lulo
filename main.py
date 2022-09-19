from Conexion.callapi import CallApi
from generic_functions.utils import Utils
from Conexion import conexion_sqlite
from etlanalisis.etl import Etl


if __name__=='__main__':
  
    ## lamada a la funcion export_json
    lis_json = CallApi().export_json()
    
    ##llamada a la funcion dataframe de la clase utils
    creating_df = Utils().dataframe(lis_json)
    
    # realizado profiling del dataframe df_embedded
    Utils().profiling(creating_df[1])
    
 
    ''' conexion a sql '''
    #conexion_sqlite.createDB()
    #conexion_sqlite.createTable()
    

    conexion_sqlite.insert(creating_df[0],"data_cruda")
    conexion_sqlite.insert(creating_df[1],"series")
    
    Etl().averageRuntime(creating_df[1])
    #Etl().genByserie(creating_df[1])