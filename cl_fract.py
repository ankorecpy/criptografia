# -*- coding: utf-8 -*-
#Archivo tomado de: http://www.jfbouch.fr/crypto/b21/b21.html
#Download Simulators B21

import sys
import string

#========== Class Fraction
class Fraction:
    def __init__(self,alpha):
        self.alpha = alpha
        self.bili = {}
        vowel = consonant = i = 0
        for letter in list(self.alpha):
            # print letter, vowel, consonant
            self.bili[letter] = [vowel,consonant]
            consonant = ( consonant + 1) % 7
            i = i + 1
            vowel = i // 7
            
    def letter2bili(self, letter):
        return self.bili[letter]

    def bili2letter(self, vowel, consonant ):
        return self.alpha[ vowel * 7 + consonant ]

if __name__ == "__main__":
    f = Fraction("LMYFXÑZOJBRSÜ«PUGCWÏ]KNTDQÀ3IHVEAÙ_\[%$,.<>/?!@#^")

    vowel = "AEIOUBC"
    consonant = "LNRSTXY"

    for letter in list("YOUR"):
        [ v, c ] = f.letter2bili( letter )
        new_letter = f.bili2letter( v, c )
        #print (letter, v,c, vowel[v], consonant[c], new_letter)

    f.info()
