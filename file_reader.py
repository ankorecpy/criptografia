""" 
	Hecho por: Alejandro Mendez Astudillo
	Descripcion: Este script lee todas las lineas de un fichero y las imprime en pantalla
"""

import sys
import os.path

def get_lines_file( _path ):
    if ( not os.path.isfile( _path ) ):
        print( "El fichero no se localiza o no existe. " +_path)
        sys.exit( )    
    file_r = open( _path, 'r', encoding="ISO-8859-1" )
    list_lines = file_r.readlines( )
    file_r.close( )
    for item in list_lines:        
        return item

def crear_Archivo(nombre, contenido):
	archivo = open(nombre, 'w', encoding="ISO-8859-1")
	archivo.write(contenido)
	archivo.close()

def print_list( _list ):
    for item in _list:
        print(item)

if __name__ == "__main__":
    if len( sys.argv ) == 2:
        lines = get_lines_file( sys.argv[ 1 ] )
        print_list( lines )
    else:
        print( "Se debe ingresar como parametro el nombre del fichero a leer con su respectiva ruta, ya sea absoluta o relativa" )
