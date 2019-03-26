# -*- coding: utf-8 -*-
""" 
	Hecho por: Alejandro Mendez Astudillo
	Descripcion: Se define la clases usada para el cifrado enigma
"""
class Disk:	
	alph_in = []
	alph_out = []
	rotations = -1	

	def __init__(self, _in, _out):
		self.alph_in = _in
		self.alph_out = _out
		self.rotations = 0
		
	def getIndexAlphIn(self, _letter):
		return self.alph_in.index(_letter)
		
	def getIndexAlphOut(self, _letter):
		return self.alph_out.index(_letter)
	
	def getLetterAlphIn(self, _index):
		return self.getLetterList(_index, self.alph_in)
		
	def getLetterAplhOut(self, _index):
		return self.getLetterList(_index, self.alph_out)
	
	def getIndexInLetter(self, _indexOut):
		letter_out = self.alph_out[_indexOut]
		return self.alph_in.index(letter_out)	
	
	def getIndexOutLetter(self, _indexIn):
		letter_in = self.alph_in[_indexIn]
		return self.alph_out.index(letter_in)
		
	def isFullRotated(self):
		return self.rotations == len(self.alph_in)
		
	def restartRot(self):
		self.rotations = 0
	
	def getLetterList(self, _index, _list):
		answer = ""
		if (_index >= 0 and _index < len(_list)):
			answer = _list[_index]
		return answer
	
	def rotateUp(self):
		auxIn, auxOut = self.alph_in[0], self.alph_out[0]		
		self.alph_in.pop(0)
		self.alph_out.pop(0)
		self.alph_in.append(auxIn)
		self.alph_out.append(auxOut)
		self.rotations = self.rotations + 1
	
