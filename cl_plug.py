# -*- coding: utf-8 -*-
#Archivo tomado de: http://www.jfbouch.fr/crypto/b21/b21.html
#Download Simulators B21

import string

class Plug:
    def __init__(self,alpha):
        self.alpha = alpha
        self.plugboard = [-1,-1,-1,-1,-1,-1,-1]

    def setAlpha(self,alpha):
        self.alpha = alpha
        self.plugboard = [-1,-1,-1,-1,-1,-1,-1]

    def zero(self):
        self.setAllPlugs( self.alpha )
        
    def getAlpha(self):        
        return self.alpha

    def setOnePlug(self, letter_in, letter_out  ):
        i_in = str.find( self.alpha, letter_in )
        i_out= str.find( self.alpha, letter_out)
        self.plugboard[ i_in ] = i_out

    def unsetOnePlug(self, letter_in ):
        i_in = str.find( self.alpha, letter_in )
        self.plugboard[ i_in ] = -1

    def unsetAllPlugs(self):
        self.plugboard = [-1,-1,-1,-1,-1,-1,-1]

    def setAllPlugs(self, key ) :
        for i in range(7):
            self.setOnePlug( self.alpha[i], key[i] )

    def isPlugged(self):
        for i in range(7):
            if self.plugboard[i] == -1: return False
        return True

    def getOnePlug(self, i ):
        return self.alpha[ self.plugboard[i] ]

    def isSrcPlugFree(self, letter):
        i_in = string.find( self.alpha, letter )
        if self.plugboard[i_in] == -1: return True
        else: return False

    def isDstPlugFree(self, letter ):
        i_in = string.find( self.alpha, letter )
        code = True
        for i in range(7):
            if self.plugboard[i] == i_in : return False
        return code

    def cipher(self, x):
        return self.plugboard[x]    

    def decipher(self, x ):
        for i in range(7):
            if self.plugboard[i] == x:
                return i
        return -1

    def getAllPlugs(self):
        ch = ""
        for i in range(7):
            ch = ch + self.getOnePlug(i)
        return ch

if __name__ == "__main__":
    p = Plug("IORSTXY")
    p.setAllPlugs("ROITSPQ")
    p.info()
    p = Plug("IORSTXY")
    p.setAllPlugs("IORSTXY")
    p.info()
    p.unsetAllPlugs()
    p.info()
    p.setOnePlug("I","R")
    p.info()
    #print ("[I=>R] I used ? (yes)", p.isSrcPlugFree("I"))
    #print ("       O used ? (no)",  p.isSrcPlugFree("O"))
    #print ("Plug   R set ? (yes)",  p.isDstPlugFree("R"))
    #print ("       T set ? (no)",   p.isDstPlugFree("T"))
    #print ("       I           ",   p.isDstPlugFree("I"))
    p.setOnePlug("O","O")
    p.setOnePlug("R","I")
    p.setOnePlug("S","T")
    p.setOnePlug("T","S")
    p.info()
    #print (p.getOnePlug(0))
    #print (p.getAllPlugs())

