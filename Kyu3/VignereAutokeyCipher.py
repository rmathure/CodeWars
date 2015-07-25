__author__ = 'rohanmathure'

'''

Write a class that, when given a key and an alphabet, can be used to encode and decode from the cipher.
E.g.

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'

# creates a cipher helper with each letter substituted
# by the corresponding character in the key
c = VigenereCipher(key, alphabet)

c.encode('codewars'); # returns 'rovwsoiv'
c.decode('laxxhsj'); # returns 'waffles'

# returns 'pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib'
c.encode('amazingly few discotheques provide jukeboxes')

# returns 'amazingly few discotheques provide jukeboxes'
c.decode('pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib')
Any character not in the alphabet should be left alone.

E.g. (following from above)

c.encode('CODEWARS') # returns 'CODEWARS'
'''
#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import codecs
import sys

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

import unittest

class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        self.key = key.decode('utf-8')
        self.abc = abc.decode('utf-8')

    def encode(self, text):
        retStr=str()
        key=str(self.key)
        keyIndex=0
        for i in range(len(text)):
            if text[i] in self.abc:
                newChar=text[i].decode('utf-8')
                retStr=retStr+self.abc[(self.abc.index(newChar)+self.abc.index(key[keyIndex]))%len(self.abc)]
                keyIndex+=1
                key=key+newChar
            else:
                retStr=retStr+text[i].decode('utf-8')

        return retStr

    def decode(self, text):
        retStr=str()
        key=str(self.key)
        newChar=str()
        keyIndex=0
        for i in range(len(text)):
            if text[i] in self.abc:
                newChar=self.abc[self.abc.index(text[i])-self.abc.index(key[keyIndex])]
                retStr=retStr+newChar
                key=key+newChar
                keyIndex+=1
            else:
                retStr=retStr+text[i]
        return retStr

class TestVignere(unittest.TestCase):
    def testVignere(self):
        key = 'password'
        abc = 'abcdefghijklmnopqrstuvwxyz'

        c = VigenereAutokeyCipher(key, abc);
        self.assertEqual(c.encode('codewars'), 'rovwsoiv')
        self.assertEqual(c.decode('laxxhsj'), 'laxxhsj')