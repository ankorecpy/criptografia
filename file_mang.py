# -*- coding: utf-8 -*-
""" 
	Hecho por: Alejandro Mendez Astudillo
	Descripcion: Este script crea y escribe sobre un fichero, tambien lee lineas de un fichero
"""

import sys
import os.path

def getLinesFile( _path ):
    file_r = open( _path, 'r', encoding="ISO-8859-1" )
    list_lines = file_r.readlines( )
    file_r.close( )
    return list_lines 

def printList( _list ):
    for item in _list:
        print( item )

def exist_file(_path):
	return os.path.isfile(_path)

def createAndWrite(path, list_lines):
	_file = open(path, "w", encoding="ISO-8859-1")
	for line in list_lines:
		_file.write(line)
	_file.close()
