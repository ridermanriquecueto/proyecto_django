try:
    with open ("TextoSistema.txt", "r") as archivo:
        contenido = archivo.read()
        print (contenido)
    archivo.close ()
except Exception as e:
    print ("error",e)
