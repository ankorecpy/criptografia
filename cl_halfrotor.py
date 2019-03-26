# -*- coding: utf-8 -*-
#Archivo tomado de: http://www.jfbouch.fr/crypto/b21/b21.html
#Download Simulators B21

import sys
import string

#========== Class HalfRotor
class HalfRotor:
    def __init__(self,nomDuRotor):
        f = open("rotors/"+nomDuRotor+".rot","r")
        self.alpha = (f.readline()).strip()
        self.nwires = len( self.alpha )
        self.perm = []
        while 1:
            ch = f.readline()
            ch = ch.strip()
            if ch == "": break
            self.perm.append(list(map(int,list(ch))))
        self.index = 0
        
    def getKey(self):
        return self.alpha[ self.index ]

    def setKey(self,key):
        self.index = str.find( self.alpha, key )

    def getPosition(self):
        return self.index

    def advance(self):
        self.index = (self.index + 1) % self.nwires

    def goBack(self):
        self.index = (self.index - 1 + self.nwires) % self.nwires

    def cipher(self,x):
        return ( self.perm[ self.index ][x] )

    def decipher(self,x):
        for i in range(7):
            if self.perm[ self.index ][i] == x :
                return i
        return (-1)

if __name__ == "__main__":
    r = HalfRotor("r1vowel")

    vowel = "AEIOUBC"

    for i in range(15):
        r.advance()
        #print (r.cipher(0), r.getKey(), r.getPosition())
    #print ("go Back")
    for i in range(7):
        r.goBack()
        #print (r.cipher(0), r.getKey(), r.getPosition())
    r.info()
