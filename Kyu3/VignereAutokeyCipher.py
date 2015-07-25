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
import unittest

class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        self.key = key
        self.abc = abc

    def encode(self, text):
        retStr=str()
        for i in range(len(text)):
            if text[i] in self.abc:
                retStr=retStr+self.abc[(self.abc.index(text[i])+self.abc.index(self.key[i]))%len(self.abc)]
            else:
                retStr=retStr+text[i]
            self.key=self.key+text[i]
        return retStr

    def decode(self, text):
        retStr=str()
        for i in range(len(text)):
            if text[i] in self.abc:
                retStr=retStr+self.abc[abs(self.abc.index(text[i])-self.abc.index(self.key[i]))]
            else:
                retStr=retStr+text[i]
        return retStr


class TestVignere(unittest.TestCase):
    def testVignere(self):
        key = 'PASSWORD';
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

        c = VigenereAutokeyCipher(key, abc);
        self.assertEqual(c.encode('AAAAAAAAPASSWORDAAAAAAAA'), 'PASSWORDPASSWORDPASSWORD')
        self.assertEqual(c.decode('PASSWORDPASSWORDPASSWORD'), 'AAAAAAAAPASSWORDAAAAAAAA')