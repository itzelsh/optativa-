carpeta_nombre="Documentos\\"
archivo_nombre="archivo_text.txt"

with open(archivo_nombre,"r") as archivo: #r es abrir el archivo modo lectura
  lineas_lista=archivo.readlines()# separa por linea
#print(lineas_lista)
num_linea=1
for linea in lineas_lista: # para que salga linea por linea
    print("num linea",num_linea,":",linea) #para indicar en que numero de linea esta 
<<<<<<< HEAD
    num_linea=num_linea+1
=======
    num_linea=num_linea+1
#Se pueden agregar mas lineas en este mismo archivo
>>>>>>> adbc8186bf38064798d74a140db0b7f5a4b4ee8c
