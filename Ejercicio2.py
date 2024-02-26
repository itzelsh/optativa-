import re
carpeta_nombre="Documentos\\"
archivo_nombre="archivo_text.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo: #la va busar como expresion por la r
      texto=archivo.read()

expresion_regular=re.compile(r"M[eéa][xr]ic?[ao](nos)?")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
  print(resultado.group(0))