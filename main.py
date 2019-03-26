# -*- coding: utf-8 -*-
import cif_enigma, cif_lorenz
from playfair import Playfair
from cl_b21 import B_21
import file_reader
import file_mang
import ayuda
import sys
from time import time

parametros = sys.argv

def path_salida(path_entrada, cifra):
	aux = path_entrada
	aux = aux.replace(".cif", "")
	aux = aux.replace(".dec", "")
	aux += ".cif" if cifra else ".dec"
	return aux

def ejecutar_enigma(entrada, clave, operacion_cifra):
	if file_mang.exist_file(entrada) and file_mang.exist_file(clave):
		salida = path_salida(entrada, operacion_cifra)
		if not file_mang.exist_file(salida):
			lineas_entrada = file_mang.getLinesFile(entrada)
			lineas_salida = cif_enigma.encrypt(lineas_entrada, clave) if operacion_cifra else cif_enigma.decrypt(lineas_entrada, clave)
			file_mang.createAndWrite(salida, lineas_salida)
			print("Proceso finalizado con exito\n")
		else:
			print("\nERROR: El fichero {0} ya existe\n" .format(salida))
	else:
		print("\nERROR: El fichero {0} no existe\n" .format(entrada))
		
def ejecutar_lorenz(entrada, clave, operacion_cifra):
	if file_mang.exist_file(entrada) and file_mang.exist_file(clave):
		salida = path_salida(entrada, operacion_cifra)
		if not file_mang.exist_file(salida):
			lineas_entrada = file_mang.getLinesFile(entrada)
			lineas_salida = cif_lorenz.encrypt(lineas_entrada, clave) if operacion_cifra else cif_lorenz.decrypt(lineas_entrada, clave)
			file_mang.createAndWrite(salida, lineas_salida)
			print("Proceso finalizado con exito\n")
		else:
			print("\nERROR: El fichero {0} ya existe\n" .format(salida))
	else:
		print("\nERROR: El fichero {0} no existe\n" .format(entrada))

def ejecutarMaqHagelin(archivo,password,cifrar):
	maqHag = B_21(password,"r1vowel","r1conso", 1)
	maqHag.setKey("AAGFHG")  # internal Wheel Key = AAAA
	if cifrar:		
		crypto = ""
		txt_in = file_reader.get_lines_file(parametros[4])
		for letter in list(txt_in):
			crypto = crypto + maqHag.cipher(letter)
		textoCifrado = archivo+".cif"
		file_reader.crear_Archivo(textoCifrado,crypto)
		print ("Archivo "+textoCifrado+" creado con exito.")       
	else:
		mensaje = ""
		txt_in = file_reader.get_lines_file(parametros[4])		
		for letter in list(txt_in):
			mensaje = mensaje + maqHag.decipher(letter)
		textoCifrado = archivo+".dec"
		file_reader.crear_Archivo(textoCifrado,mensaje)
		print ("Archivo "+textoCifrado+" creado con exito.")  


if len(parametros) == 1:
	ayuda.ayudaPrincipal()
elif len(parametros) == 3:
	if (parametros[1] == "-pf" and parametros[2] == "-a"):				
		ayuda.ayudaAlgoritmo("-pf")
	elif (parametros[1] == "-ks" and parametros[2] == "-a"):				
		ayuda.ayudaAlgoritmo("-ks")
	elif (parametros[1] == "-mh" and parametros[2] == "-a"):				
		ayuda.ayudaAlgoritmo("-mh")
	elif (parametros[1] == "-lz" and parametros[2] == "-a"):				
		ayuda.ayudaAlgoritmo("-lz")
	elif (parametros[1] == "-me" and parametros[2] == "-a"):				
		ayuda.ayudaAlgoritmo("-me")
	else:
		ayuda.ayudaEspecifica()		
elif len(parametros) == 7:
	if (parametros[1] == "-pf" and parametros[2] == "-c" and parametros[3]=="-e" and parametros[5] == "-k"):						
		print ("Cifrando...")
		txt_in = file_reader.get_lines_file(parametros[4])
		password = file_reader.get_lines_file(parametros[6])
		textoCifrado = parametros[4]+".cif"
		cifra = Playfair()
		start_time = time()
		cifrado = cifra.pf_Cifrar(txt_in, password)		
		file_reader.crear_Archivo(textoCifrado,cifrado)
		print ("Archivo "+textoCifrado+" creado con exito.")
		elapsed_time = time() - start_time
		print ("Total tiempo: %.10f segundos." % elapsed_time)
	elif (parametros[1] == "-pf" and parametros[2] == "-d" and parametros[3]=="-e" and parametros[5] == "-k"):
		print ("Descifrando...")
		txt_in = file_reader.get_lines_file(parametros[4])		
		password = file_reader.get_lines_file(parametros[6])			
		cifra = Playfair()
		start_time = time()
		mensaje = cifra.pf_descifrar(txt_in,password)
		mensaje = mensaje.replace('$','') # Reemplazar caracter por la Integridad del arcihvo.
		miArchivo = parametros[4].split('.')
		archivo = miArchivo[0]+"."+miArchivo[1]+".dec"
		file_reader.crear_Archivo(archivo,mensaje)		
		print ("Archivo "+archivo+" creado con exito.")
		elapsed_time = time() - start_time
		print ("Total tiempo: %.10f segundos." % elapsed_time)
	elif (parametros[1] == "-me" and parametros[2] == "-c" and parametros[3]=="-e" and parametros[5] == "-k"):
		print("Cifrando...")
		start_time = time()
		ejecutar_enigma(parametros[4], parametros[6], True)
		elapsed_time = time() - start_time
		print ("Total tiempo: %.10f segundos." % elapsed_time)
	elif (parametros[1] == "-me" and parametros[2] == "-d" and parametros[3]=="-e" and parametros[5] == "-k"):
		print("Descifrando...")
		start_time = time()
		ejecutar_enigma(parametros[4], parametros[6], False)
		elapsed_time = time() - start_time
		print ("Total tiempo: %.10f segundos." % elapsed_time)	
	elif (parametros[1] == "-lz" and parametros[2] == "-c" and parametros[3]=="-e" and parametros[5] == "-k"):
		print("Cifrando...")
		start_time = time()
		ejecutar_lorenz(parametros[4], parametros[6], True)
		elapsed_time = time() - start_time
		print ("Total tiempo: %.10f segundos." % elapsed_time)
	elif (parametros[1] == "-lz" and parametros[2] == "-d" and parametros[3]=="-e" and parametros[5] == "-k"):
		print("Cifrando...")
		start_time = time()
		ejecutar_lorenz(parametros[4], parametros[6], False)
		elapsed_time = time() - start_time
		print ("Total tiempo: %.10f segundos." % elapsed_time)
	elif (parametros[1] == "-mh" and parametros[2] == "-c" and parametros[3]=="-e" and parametros[5] == "-k"):
		print("Cifrando...")
		start_time = time()		
		ejecutarMaqHagelin(parametros[4], parametros[6],True)
		elapsed_time = time() - start_time
		print ("Total tiempo: %.10f segundos." % elapsed_time)		
	elif (parametros[1] == "-mh" and parametros[2] == "-d" and parametros[3]=="-e" and parametros[5] == "-k"):
		print("Descifrando...")
		start_time = time()		
		ejecutarMaqHagelin(parametros[4], parametros[6],False)
		elapsed_time = time() - start_time
		print ("Total tiempo: %.10f segundos." % elapsed_time)		
	
	else:
		ayuda.ayudaEspecifica()
else:
	print ("Faltan Argumentos.")
	ayuda.ayudaEspecifica()

