from asyncore import write
from pydoc import html
from tkinter.ttk import Style
from xml.etree.ElementInclude import include
import pandas as pd
import numpy as np
import pandas_profiling
from pandas_profiling.utils.cache import cache_file



class Utils:

    def dataframe(self, data):
        '''dataframe:{ 
            args: data,
            funcion: crear dos dataframe "df_output" y "df_embedded"
            df_output contiene todos los datos obtenidos por la Api en la forma mas cruda.
            df_embedded es un data frame que contiene los datos de la key("_embedded"), df_embedded nos dice las caracteristmas de las series 
        '''
        
        
        for i in range(len(data)):
            if i == 0:
                df_output = pd.DataFrame(data[i])
            else:
                df_muestra = pd.DataFrame(data[i])
                df_output = pd.concat([df_output,df_muestra])

        for row in range(len(df_output)):
            if row == 0:
                df_show = pd.DataFrame([df_output["show"].iloc[0]])
                # df_show = df_show.T
            else:
                df_muestra2 = pd.DataFrame([df_output["show"].iloc[row]])
                # df_muestra2 = df_muestra2.T
                df_show = pd.concat([df_show,df_muestra2])
                 
        df_show = df_show.drop_duplicates(subset=["name"])
        
            
        # with pd.ExcelWriter("prueba.xlsx") as writer:
        #     df_output.to_excel(writer, sheet_name="ejemplo")
        #     df_show.to_excel(writer, sheet_name="ejemplo2")

        return(df_output,df_show)

    def profiling(self,df):
        '''profiling:{ 
            args: df,
            funcion: tomo como argumento el df_embedded  realiza un reporte en html de las estadisticas de las variables de este dataframe
        '''
        report = df.profile_report(sort = None, html = {"Style":{"full_width":True}})
        report.to_file(output_file=("profiling.html"))
    
  
        
        

