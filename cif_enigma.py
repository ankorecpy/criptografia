# -*- coding: utf-8 -*-
""" 
	Hecho por: Alejandro Mendez Astudillo
	Descripcion: Este script realiza el cifrado y descifrado de ficheros, todo esto haciendo uso del algoritmo de cifrado enigma
"""
import sys
import base64
from classes_enigma import Disk
import file_mang as _file

def _encrypt_line(_line, _disks):
	answer = ""	
	for caracter in _line:		
		indexIn = _disks[0].getIndexAlphIn(caracter)
		newIndex = _encrypt_caracter(indexIn, _disks, 0)
		answer = answer + _disks[0].getLetterAlphIn(newIndex)
		_validUpRotations(_disks[:len(_disks) - 1])	
	return answer
	
def _decrypt_line(_line, _disks):
	answer = ""	
	for caracter in _line:		
		indexIn = _disks[0].getIndexAlphIn(caracter)
		newIndex = _decrypt_caracter(indexIn, _disks, 0)
		answer = answer + _disks[0].getLetterAlphIn(newIndex)
		_validUpRotations(_disks[:len(_disks) - 1])	
	return answer

def _encrypt_caracter(_indexLetter, _disks, _indexDisk):
	disk = _disks[_indexDisk]
	answer = disk.getIndexOutLetter(_indexLetter)
	if _indexDisk < (len(_disks) - 1):
		index_out = _encrypt_caracter(answer, _disks, _indexDisk + 1)
		answer = disk.getIndexInLetter(index_out)		
	return answer
	
def _decrypt_caracter(_indexLetter, _disks, _indexDisk):
	disk = _disks[_indexDisk]
	answer = 0
	answer = disk.getIndexInLetter(_indexLetter) if _indexDisk == (len(_disks) - 1) else disk.getIndexOutLetter(_indexLetter)
	if _indexDisk < (len(_disks) - 1):
		index_out = _decrypt_caracter(answer, _disks, _indexDisk + 1)
		answer = disk.getIndexInLetter(index_out)		
	return answer

def _getDisks(path):
	linesConfig = _file.getLinesFile(path)
	disk1 = Disk(list(linesConfig[0].rstrip('\n')), list(linesConfig[1].rstrip('\n')))
	disk2 = Disk(list(linesConfig[2].rstrip('\n')), list(linesConfig[3].rstrip('\n')))
	disk3 = Disk(list(linesConfig[4].rstrip('\n')), list(linesConfig[5].rstrip('\n')))
	reflex = Disk(list(linesConfig[6].rstrip('\n')), list(linesConfig[7].rstrip('\n')))
	return [disk1, disk2, disk3, reflex]
	
def _validUpRotations(_disks):
	rotate = True
	for disk in _disks:
		if rotate:
			disk.rotateUp()
			rotate = disk.isFullRotated()
		else:
			break
			
def _clean_line(line, symbol):
	waste = ""
	if symbol in line:
		line.rstrip(symbol)
		waste = symbol
	return waste
	
def encrypt(lines, path_config):
	disks = _getDisks(path_config)
	cryptedLines = []
	for line in lines:
		waste = _clean_line(line, '\n')
		cleanedLine = line
		codedLine = (base64.encodestring(cleanedLine.encode())).decode()
		codedLine = codedLine.replace('\n',"")
		cryptedLine = _encrypt_line(codedLine, disks)
		cryptedLines.append(cryptedLine + waste)
	return cryptedLines

def decrypt(lines, path_config):
	disks = _getDisks(path_config)
	decodedLines = []
	for line in lines:
		cleanedLine = line.rstrip('\n')
		decryptedLine = _decrypt_line(cleanedLine, disks)		
		decodedLine = (base64.decodestring(decryptedLine.encode()))
		decodedLine = decodedLine.decode()
		decodedLines.append(decodedLine)
	return decodedLines
