"""
Security I.
http://www.cl.cam.ac.uk/teaching/1112/SecurityI/

Assume strings use alphabet A-Z.
"""

import string
import scipy.stats

def alpha_to_int(char):
    base = ord("A")
    return ord(char.upper())-base
    
def int_to_alpha(int):
    base = ord("A")
    return chr(int+base).upper()

def shift(str,n):
    return "".join(map(lambda char: int_to_alpha((alpha_to_int(char)+n)%26),str))
    
def all_shifts(str):
    return [shift(str,i) for i in range(0,25)]

class Bijection(dict):
    """
    Very simple implementation of a bijection. Does not check that one to one
    mapping is enforced.
    """
    
    def __init__(self,*args,**kwargs):
        dict.__init__(self,args,kwargs)
        
    def flipped():
        """
        Creates a new Bijection with domain and range flipped.
        """
        return Bijection([[v,k] for k,v in self.items()])
    
def substitution(str,permutation):
    def substitute(char):
        if char in permutation:
            return permutation[char]
        else:
            return char
    
    return "".join(map(substitute,str))
    
def vigenere_encrypt(p,k):
    c = [0] * len(p) # Just to make clear later on
    for i in range(0,len(p)):
        # For each element of p need to perform some operation f(p[i],k[i])
        # however don't want to demand key to be as long as the plain text
        # so repeat key.
        c[i] = ( alpha_to_int(p[i]) + alpha_to_int(k[i%len(k)]) ) % 26
    return ''.join(int_to_alpha(i) for i in c)
    
def vigenere_decrypt(c,k):
    p = [0] * len(c)
    for i in range(0,len(c)):
        p[i] = ( alpha_to_int(c[i]) - alpha_to_int(k[i%len(k)]) ) % 26
    return ''.join(int_to_alpha(i) for i in p)
    
def profile(s):
    """
    Counts occurences of characters in string.
    Use ? for any character that is not A-Z.
    """
    
    counts = dict(zip(string.uppercase,[0]*26))
    total_alpha = 0
    for k in counts:
        k_count = s.count(k)
        counts[k] = k_count
        total_alpha += k_count
    counts["*"] = len(s)-total_alpha
    return counts
    
def vigenere_profile_position(ciphertext,key_length,key_pos):
    """
    Profiles ciphertext for a particuliar position in key.
    """
    assert key_pos >= 0 and key_pos < key_length
    ciphertext_at_pos = ''.join(ciphertext[i+key_pos] for i in range(0,len(ciphertext)-key_length,key_length))
    return profile(ciphertext_at_pos)
    
class VigenereProfile():
    position = None
    distribution = None
    def __init__(self,position,distribution):
        self.position = position
        self.distribution = distribution
    def __repr__(self):
        return "%s: %s" % (self.position,self.distribution)
    
def vigenere_profile_all_positions(ciphertext,key_length):
    """
    Profiles ciphertext for all positions in key.
    """
    result = []
    for key_pos in range(0,key_length):
        result.append(VigenereProfile(key_pos,vigenere_profile_position(ciphertext,key_length,key_pos)))
    return result
    
def chunks(s,chunk_period,offset=0,chunk_length=1):
    """
    Get a string made up of chunks of specified length taken from specified string
    at specified intervals starting at specified offset.
    """
    return ''.join(s[i:i+chunk_length] for i in range(offset,len(s),chunk_period))
    
def dict_values_sorted(d):
    """
    Get values from dictionary d sorted by key.
    """
    return [v for k,v in sorted(d.items())]
    
def vigenere_guess_key_character(ciphertext,plaintext_distribution,key_length,key_pos):
    """
    For a given cipher text, plain text distribution and key length find the best key
    character for a given position by comparing distribution of cipher text to
    plain text.
    """
    
    ciphertext_at_pos = chunks(ciphertext,key_length,key_pos)
    best_k_char = None
    best_correlation_coeffecient = -1
    for k_char in string.uppercase:
        decrypted_dist = profile(vigenere_decrypt(ciphertext_at_pos,k_char))
        # Compare the ranking of characters in distribution of plain text
        # and of decrypted cipher text using k_char.
        (correlation_coeffecient,p_value) = scipy.stats.spearmanr(
            dict_values_sorted(plaintext_distribution),
            dict_values_sorted(decrypted_dist)
        )
        if correlation_coeffecient > best_correlation_coeffecient:
            best_k_char = k_char
            best_correlation_coeffecient = correlation_coeffecient
    return (best_k_char,best_correlation_coeffecient)
    
def vigenere_guess_key_with_length(ciphertext,plaintext_distribution,key_length):
    guess = []
    for i in range(0,key_length):
        guess.append(vigenere_guess_key_character(ciphertext,plaintext_distribution,key_length,i))
    return guess
    
def mean(values,key=lambda x: x):
    return sum(map(key,values))/len(values)
    
class VigenereGuess():
    
    key_length = None
    guess = None
    # How good the key is as a function of the correlation coeffecients
    # from distribution of cipher text decrypted by individual key characters.
    goodness = None
    key = None
    
    def __init__(self,key_length,guess):
        self.key_length = key_length
        self.guess = guess
        self.goodness = mean(guess,lambda x: x[1])
        self.key = ''.join(c_guess[0] for c_guess in guess)
        
    def __repr__(self):
        return "VigenereGuess(key_length: %s, key: %s, goodness: %s, guess: %s)" % (self.key_length,self.key,self.goodness,self.guess)
        
    def __cmp__(self,other):
        return cmp(other.goodness,self.goodness)
        
    
def vigenere_guess_key(ciphertext,plaintext_distribution,key_length_low,key_length_high,verbose=True):
    """
    Uses plain text distribution to guess key.
    """
    assert key_length_low > 0 and key_length_low <= key_length_high
    
    guesses = []
    for key_length in range(key_length_low,key_length_high):
        guess = vigenere_guess_key_with_length(ciphertext,plaintext_distribution,key_length)
        vg = VigenereGuess(key_length,guess)
        guesses.append(vg)
        if verbose: print vg
    
    guesses.sort()
    if verbose: print guesses[0]
    return guesses[0].key
    
def vigenere_crack(ciphertext,plaintext_distribution):
    
    key = vigenere_guess_key(ciphertext,plaintext_distribution,1,30)
    return vigenere_decrypt(ciphertext,key)