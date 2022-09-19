import requests
import json
import datetime
from datetime import date

class CallApi:
    
    '''Class CallApi
        contiene dos funciones get_data y export_json          
    '''
        
    def get_data(self,url):
        '''get_data:{ 
            args: url,
            funcion: realiza una petición a la API si la respuesta del servidor es correcta,
            entonces crea una lista vacia "lis_data" y mediante un ciclo le agrega los elementos obtenidos de los datos enviados por la API,
            return : lis_data
        '''
        
        data = requests.get(url)
        if data.status_code == 200:
            data = data.json()
                        
           
            lis_data = []        
            for element in data:     
                lis_data.append(element) 
                  
            return(lis_data)
                                            
        else: 
            print(data.status_code)
                   

    def export_json(self):
        '''export_json:{ 
            args: None,
            funcion: (para la fecha seleccionada "diciembre/2020" hacemos la petición a la API  llamando a la funcion get_data,
            la cual le pasamos como argumento una URL que va a cambiar la fecha medienta un ciclo for.
            el resultado de cada llamada la almacenamos a una lista "lis_json", 
            porsteriomente recorremos la lista "lis_json" para obtener cada elemento y escribirlo en un archivo "data.json",)

            return: lis_json
        '''
        lis_json = []
        for i in range(31):
            day = date(2020,12,1)        
            sumday = day + datetime.timedelta(days=i)
            #url = (f'http://api.tvmaze.com/schedule/web?date={sumday}')
            url = (f'http://api.tvmaze.com/schedule?date={sumday}')
            lis_data = CallApi().get_data(url)
            lis_json.append(lis_data)

        filename = ".\json\data.json"
        with open(filename,"w") as file:
            for element in lis_json:
                json.dump(element,file,indent=4)
        return lis_json




        
      
                
