# -*- coding: ISO-8859-1 -*-
#Archivo tomado de: http://www.jfbouch.fr/crypto/b21/b21.html
#Download Simulators B21

import sys
import os.path
import string
from cl_wheel import * 
from cl_fract import * 
from cl_halfrotor import *
from cl_plug  import *

#========== Class B_21
class B_21:
    def __init__(self,key_base,rot_vow,rot_con,debug):
        self.w = []
        self.w.append( Wheel("ABCDEFGHIJKLMNÑOPQRSTUVWXYZÜ«Ï]À3Ù_\[%$,.<>/?!@#^",7  ) )
        self.w.append( Wheel("ABCDEFGHIJKLMNÑOPQRSTUVWXYZÜ«Ï]À3Ù_\[%$,.<>/?!@",6  ) )
        self.w.append( Wheel("ABCDEFGHIJKLMNÑOPQRSTUVWXYZÜ«Ï]À3Ù_\[%$,.<>/?",8  ) )
        self.w.append( Wheel("ABCDEFGHIJKLMNÑOPQRSTUVWXYZÜ«Ï]À3Ù_\[%$,.<>",7  ) )    
        f = open(key_base, "r")
        ch = f.readline().strip()        
        self.keyboard = Fraction(ch)        
        ch = f.readline().strip()        
        self.lights_and_keys = ch
        ch = f.readline().strip()
        tb = ch.split(":")        
        self.plug_vow = Plug( tb[0] )
        self.plug_vow.setAllPlugs( tb[1] ) 
        ch = f.readline()
        ch = ch.strip()
        tb = ch.split(":")
        self.plug_con = Plug( tb[0] )
        self.plug_con.setAllPlugs( tb[1] )
        self.nw = 4
        for i in range( self.nw ):
            ch = f.readline()
            ch = ch.rstrip()
            lg = len(ch)
            for j in range(lg):
                if ch[j] != '.':
                    self.w[i].setPinsON( ch[j] )
        self.rot_vow = HalfRotor(rot_vow)
        self.rot_con = HalfRotor(rot_con)
        if ( debug ): self.DEBUG = 1 
        else: self.DEBUG = 0
        self.debug_info = ""

    def advance(self):
        global theWheels
        theWheels = " : "
        # 1 - Advance Wheels 
        for i in range( self.nw ):            
            self.w[i].turnClockwise()
            if ( self.DEBUG ):
                #print self.w[i].getExternalKey(),
                theWheels += str( self.w[i].isActive() ) + " "
                #print self.w[i].isActive(),
                #print self.w[i].getExternalShiftedKey(),

        # 2 - Advance Half-Rotors
        if ( self.w[0].isActive() or self.w[1].isActive() ):
            self.rot_vow.advance()
        if ( self.w[2].isActive() or self.w[3].isActive() ):
            self.rot_con.advance()    

        if ( self.DEBUG ):
            theWheels += " : "
            theWheels +=  self.rot_vow.getKey() + " "
            theWheels +=  self.rot_con.getKey()
            theWheels += " ! "

    def goBack(self):
        # 2 - go Back Half-Rotors
        if ( self.w[0].isActive() or self.w[1].isActive() ):
            self.rot_vow.goBack()
        if ( self.w[2].isActive() or self.w[3].isActive() ):
            self.rot_con.goBack()    

        # 1 - go Back Wheels 
        for i in range( self.nw ):
            self.w[i].turnCounterClockwise()
            if ( self.DEBUG ):
                pass
                #print self.w[i].getExternalKey(),
                #print self.w[i].isActive(),
                #print self.w[i].getExternalShiftedKey(),

        if ( self.DEBUG ):
            pass
            #print self.rot_vow.getKey(),
            #print self.rot_con.getKey(),
            
    def cipher(self, letter ):
        global theWheels
        # 1 - Advance wheel and half-rotors
        self.advance()
                
        # 2 - Keyboard ( plain letter -> biliterals )
        [ v, c ] = self.keyboard.letter2bili( letter )
        
        # 3 - Cipher v and c
        v = self.rot_vow.cipher( v )
        c = self.rot_con.cipher( c )        

        # 4 - Plugboard
        v = self.plug_vow.cipher( v )
        c = self.plug_con.cipher( c )        

        # 5 - Lampboard ( biliterals -> cipher letter)
        new_letter = self.keyboard.bili2letter( v, c )
        
        return new_letter

    def decipher(self, letter ):
        global theWheels        

        # 1 - Advance wheels and half-rotors
        self.advance()

        # 2 - Keyboard ( plain letter -> biliterals )
        [ v, c ] = self.keyboard.letter2bili( letter )

        # 3 - Plugboard
        v = self.plug_vow.decipher( v )
        c = self.plug_con.decipher( c )

        # 4 - Cipher v and c
        v = self.rot_vow.decipher( v )
        c = self.rot_con.decipher( c )
        
        # 5 - Lampboard ( biliterals -> cipher letter)
        new_letter = self.keyboard.bili2letter( v, c )
        
        return new_letter

    def setKey(self, key ):
        self.rot_vow.setKey( key[0] )
        self.rot_con.setKey( key[1] )
        for i in range( self.nw ):
            self.w[i].setKey( key[ i + 2 ] )

    def getMsgKey(self):
        ch = ""
        ch = ch + self.rot_vow.getKey()
        ch = ch + self.rot_con.getKey()
        for i in range( self.nw ):
            ch = ch + self.w[i].getExternalKey()
        return ch

    def zero(self):
        self.rot_vow.setKey("A")
        self.rot_con.setKey("A")
        for i in range( self.nw ):
            self.w[i].zero()
        self.plug_con.zero()
        self.plug_vow.zero()
        self.resetHistory()

    def getHistory(self):
        return self.debug_info

    def toggleDebug(self):
        if self.DEBUG : 
            self.DEBUG=0
            self.resetHistory()
        else: 
            self.DEBUG=1
        return self.DEBUG

    def resetHistory(self):
        self.debug_info = ""

#========== Debut Programme
if __name__ == "__main__":

    m = B_21("r1base","r1vowel","r1conso", 1)
    m.setKey("AAGFHG")  # internal Wheel Key = AAAA

    plain = "HASTEMAKESWASTE"
    print (plain)
    crypto = ""
    for letter in list(plain):
        crypto = crypto + m.cipher( letter )
    #print (crypto)

    print ("A try of deciphering")
    m.setKey("AAGFHG")  # internal Wheel Key = AAAA
    #crypto= "NCYQHBWIUPESDAEHUDRLUMYFYPQUUXAWMBNRIQCTTJLIWOYLMB"
    plain = ""
    for letter in list(crypto):
        plain = plain + m.decipher( letter )
    print (plain)
    #print
    m.setKey("AAAAAA")
    m.advance() ; print
    m.advance() ; print
    m.advance() ; print
    m.goBack()  ; print
    m.goBack()  ; print
    m.goBack()  ; print