import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Etl:


    def averageRuntime(self,df):
        ''' averageRuntime por tipo (type) por mes.'''
        df_avruntime = df.groupby(['type'])[['averageRuntime']].mean()
        df_avruntime = df_avruntime.sort_values(by=["averageRuntime"],ascending=False)

        #graficas
        x = df_avruntime.index
        y = df_avruntime["averageRuntime"]
        plt.barh(x,y,color = "orange")
        plt.title("Average RunTime by type")
        plt.legend(loc = 'upper right')
        plt.grid()
        plt.show()
        return (df_avruntime)

    # def genByserie(self,df):
    #     column_genres = np.array([df['genres']])
    #     genero_por_series = []

    #     for i in range(len(df['genres'])):
    #         bad_chars = [',', ']', '[', "'"]
    #         test_string = column_genres[0][i]
            
    #         test_string = ''.join((filter(lambda x: x not in bad_chars, test_string)))
            
    #         list_gender = test_string.split()
    #         genero_por_series.append(list_gender)

        
    #     serie_gender = pd.DataFrame(genero_por_series, columns=["gener1","gener2","gener3","gener4",])
        
        
                      
    #     serie_gender['name'] = np.array(df['name'])
        
        
        # serie_gender = serie_gender.rename(columns={0:"gener1",1:"gener2",2:"gener3", 3:"gener4"})
       
        # df_genres = serie_gender.groupby(['gener1'])['name'].count()
        # df_genres2 = serie_gender.groupby(['gener2'])['name'].count()
        # df_genres3 = serie_gender.groupby(['gener3'])['name'].count()
        # df_genres4 = serie_gender.groupby(['gener4'])['name'].count()

        # unido = pd.concat([df_genres,df_genres2,df_genres3,df_genres4],axis=1)
        # unido["total"] = unido.sum(axis=1)

        # ##grafica
        # x = unido.index
        # y = unido["total"]
        # plt.barh(x,y,color = "#a349a4")
        # plt.title("cantidad de series por genero")
        # plt.legend(loc = 'upper right')
        # plt.grid()
        # plt.show()

        #return(unido)


