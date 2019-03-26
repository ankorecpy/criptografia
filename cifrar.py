# -*- coding: utf-8 -*-
"""
	Metodos basicos para cifrar.
    Realizado por: Jorge Tunubalá
"""

class Cifrar(object):    

    alfabetoSimbolico = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÜ«Ï]À3Ù_\[%$,.<>/?!@#^"

    def formato(self, texto):
        """Retorna el texto sin espacios y en mayusculas."""
        return texto.replace(' ','').upper()

    def crear_Matriz(self, key = ''):
        #Devuelve un alfabeto en una matriz de 7x7. Por defecto, devuelve una matriz formada por el alfabeto ABCDEFGHIKLMNOPQRSTUVWXYZ
        matriz = []
        num = 7
        alfabeto = self.alfabetoSimbolico
        alfabeto = self.crear_Alfabeto(key, alfabeto)
        for i in range(0, len(alfabeto), num):
            fila = alfabeto[i:i + num]                
            matriz.append(fila)
        return matriz

    def crear_Alfabeto(self, key = '', alfabeto = alfabetoSimbolico):
        """Devuelve un alfabeto con key como clave y al inicio del alfabeto"""
        if key:       
            key = key.replace(' ','')
            key = key.upper()              
            temp = ''
            """Eliminar caracteres repetidos en la clave"""
            for caracter in key:
                if caracter not in temp:
                    temp += caracter
            key = temp                      
        """Eliminar los valores que contenga la clave en el alfabeto."""
        for caracter_Key in key:
            if caracter_Key in alfabeto:
                alfabeto = alfabeto.replace(caracter_Key, '')        
        return key + alfabeto
