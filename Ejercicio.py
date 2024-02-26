#Cuente las lineas que contiene el archivo y lo indique
#Cuando encuentre una linea que no contenga texto, indique
#que esa linea esta vacia
#Muestre cuantas lineas tienen texto y cuantas no
carpeta_nombre="Documentos\\"
archivo_nombre="archivo_text.txt"

with open(archivo_nombre,"r") as archivo: #r es abrir el archivo modo lectura
  lineas_lista=archivo.readlines()# separa por linea
#print(lineas_lista)
num_linea=1
lineas_totales=len(lineas_lista)#sacas el total de lineas
lineas_vacias=0
lineas_texto=0
for linea in lineas_lista: # para que salga linea por linea
    if linea.strip()=="": # strip es para identificar las lineas vacias y omitirlas 
        print("linea vacia",linea)
        lineas_vacias=lineas_vacias+1
        continue #continue es para continuar con la siguientes linea, permite que siga ejucutando
    print("Linea",num_linea,":",linea)
    lineas_texto=lineas_texto+1
    num_linea=num_linea+1
print("Este es el total de lineas",lineas_totales)
print("Estas son las lineas vacias",lineas_vacias)
print("Estas lineas contienen texto",lineas_texto)