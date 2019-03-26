# -*- coding: utf-8 -*-
"""
	Clase PlayFair: Metodos basicos para cifrar y descifrar texto
	mediante el algoritmo PlayFair.

	Elaborado por: Jorge Tunubalá
"""
import sys
from cifrar import Cifrar
password = ''
 
class Playfair(Cifrar):
	def pf_Cifrar(self, texto, clave):
		password = clave
		"""Vuelve el texto cifrado con la cifra de Playfair con una clave que se utilizará."""
		textoCifrado = ''        
		texto = texto.upper()
		texto = texto.replace(' ', '') 

		"""Rompe una pareja de letras iguales insertando una letra en medio de ellas."""
		texto = self.romper_Pareja(texto)
			
		""" Concatenar una letra si el tamaño del texto es impar."""		
		if len(texto) % 2:			
			texto += '$'			

		"""Obtener matriz de playfair."""		
		self.matriz = self.crear_Matriz(password)		
		for i in range(0, len(texto), 2):                         			
			textoCifrado += self.convertir_Pareja(texto[i:i + 2])			
		return textoCifrado.upper()

	def pf_descifrar(self, criptograma, clave):
		password = clave
		mensaje = ''
		for i in range(0, len(criptograma), 2):                         
			mensaje += self.convertir_Pareja(criptograma[i:i + 2], True)           
		return mensaje.upper()

	def romper_Pareja(self, texto):		
		salida = ''
		for letra in range(0, len(texto), 2):			
			pareja = texto[letra:letra+2]				
			if len(pareja) > 1 and pareja[0] == pareja[1]:				
				salida += pareja[0] + '$' + pareja[1]
			else:
				salida += pareja		
		return salida

	def convertir_Pareja(self, pareja, descifrar = False):
		"""Devuelve los nuevos caracteres de un par de letras a partir de la matriz"""
		# retorno - valor que se devuelve cuando se alcanza el límite de la tabla.
		# limite - valor de límite de las celdas de la tabla
		# paso - valor de incremento/decremento										
		if descifrar:
			retorno = 6
			limite = -1
			paso = -1
		else:
			retorno = 0
			limite = 7
			paso = 1        
		coord1, coord2 = self.coordenadas(pareja)			
		if coord1[0] == coord2[0]:
			# Caso en que las letras estan en la misma fila
			coord1[1] += paso
			coord2[1] += paso
		elif coord1[1] == coord2[1]:
			# Caso en que las letras estan en la misma columna
			coord1[0] += paso
			coord2[0] += paso			
		else:
			# Caso en que las letras estan en diferente fila y columna
			coord1[1], coord2[1] = coord2[1], coord1[1]
		coord1 = [retorno if x == limite else x for x in coord1]
		coord2 = [retorno if x == limite else x for x in coord2]
		return self.caracter(coord1) + self.caracter(coord2)

	def coordenadas(self, pareja):
		"""Devuelve las coordenadas de un par de letras en una matriz.""" 		
		coordenadas = []
		self.matriz = self.crear_Matriz(password)				
		for caracter in pareja:			
			for linea in range(len(self.matriz)):			    
			    if caracter in self.matriz	[linea]:
			        coordenadas.append([linea, self.matriz[linea].index(caracter)])
			        break        
		return coordenadas
 
	def caracter(self, coord):
		"""Devuelve caracter con la coordenada dada"""
		self.matriz = self.crear_Matriz(password)	
		return self.matriz[coord[0]][coord[1]]