import numpy  as np
import pandas as pd
#Alexander Salazar NC = 0139
#3 datos matriz 4 x 3
datos_alumnos = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombres a las columnna
#almacenar la tabla en la variable df dataframe
print("----datos matriz 4 x 3----")
df=pd.DataFrame(datos_alumnos,columns=['ci','marca','paquete'])
print(df)
#datos a partir de un diccionario
print("----datos a partir de un diccionario----")
alumnos_diccionario = {
    "nombre":["Alexander","pau","abi","valeria","mabel","parra"],
    "califa":[90,100,80,70,50,90],
    "edad":[64,15,16,16,18,15]
}

estudiantes = pd.DataFrame(alumnos_diccionario)
print(estudiantes)
print("Alexander Salazar nc= 0139")