# -*- coding: utf-8 -*-
#Archivo tomado de: http://www.jfbouch.fr/crypto/b21/b21.html
#Download Simulators B21

import string

class Wheel:
    def __init__(self,alphabet,shift):
        self.alphabet = alphabet
        self.lg = len(alphabet)
        self.pins = []
        for i in range(self.lg):
            self.pins.append( 0 )
        self.position = 0
        self.shiftWindow = shift

    def setPinsON(self,car):
        i = str.find(self.alphabet,car)
        self.pins[i] = 1

    def setPinsOFF(self,car):
        i = str.index(self.alphabet,car)
        self.pins[i] = 0
        
    def getAPins(self,car):
        i = str.index(self.alphabet,car)
        return self.pins[i]

    def getShift(self):
        return self.shiftWindow

    def turnClockwise(self):
        self.position = (self.position + 1 ) % self.lg

    def turnCounterClockwise(self):
        self.position = (self.position + self.lg - 1 ) % self.lg 

    def getLg( self):
        return len( self.alphabet )

    def getPosition(self):
        return self.position

    def setPosition(self, newPosition ):
        self.position = newPosition

    def setKey(self, letter_key ):
        i = str.find( self.alphabet, letter_key )
        self.setPosition( i )

    def getExternalKey(self):
        return self.alphabet[ self.position ]

    def getExternalShiftedKey(self):
        return self.alphabet[(self.position + self.shiftWindow)%self.lg]

    def getInternalKey(self):
        ch = ""
        for i in range(self.lg):
            if self.pins[i] :
                ch = ch + self.alphabet[i]
            else:
                ch = ch + "_"
        return ch

    def isActive(self):
        pos_active = ( self.position + self.shiftWindow ) % self.lg
        if self.pins[ pos_active ] != 0:
            return 1
        else:
            return 0

    def zero(self):
        self.position = 0
        for i in range(self.lg):
            self.pins[i] = 0

if __name__ == "__main__":
    un_wheel = Wheel("ABCDEFGHIKLMNOPQR",10  ) 

    for letter in list("BCFILNP"):
        un_wheel.setPinsON( letter )

    un_wheel.info()
