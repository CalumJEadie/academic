#! /usr/bin/env python

import security
import plain_texts
import scipy.stats

# Q2.

def q2():
    cipher_text = 'LUXDZNUAMNDODJUDTUZDGYQDLUXDGOJDCKDTKKJDOZ'
    permutation = {'x':' '}

    shifted_cipher_texts = security.all_shifts(cipher_text)
    plain_texts = [security.substitution(s,permutation) for s in shifted_cipher_texts]

    print '\n'.join(plain_texts)

# Q3.

def q3():
    
    p4 = plain_texts.p4
    print p4[0:200]
    p4_dist = security.profile(p4)
    print p4_dist
    key = "SECRET"
    c4 = security.vigenere_encrypt(p4,key)
    print c4[0:200]
    print security.vigenere_guess_key_character(c4,p4_dist,len(key),0)
    print security.vigenere_guess_key_with_length(c4,p4_dist,len(key))
    print security.vigenere_guess_key(c4,p4_dist,3,10)
    print security.vigenere_crack(c4,p4_dist)[0:200]
    
q3()