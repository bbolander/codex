#!/usr/bin/python
# Goat Latin is a made-up language based off of English, sort of like Pig Latin.
# The rules of Goat Latin are as follows:
# 1. If a word begins with a consonant (i.e. not a vowel), remove the first
#    letter and append it to the end, then add 'ma'.
#    For example, the word 'Goat' becomes 'oatGma'.
# 2. If a word begins with a vowel, append 'ma' to the end of the word.
#    For example, the word 'Uber' becomes 'Uberma'.
# 3. Add one letter "a" to the end of each word per its word index in the
#    sentence, starting with 1. That is, the first word gets "a" added to the
#    end, the second word gets "aa" added to the end, the third word in the
#    sentence gets "aaa" added to the end, and so on.

# Write a function that, given a string of words making up one sentence, returns
# that sentence in Goat Latin. For example:
#
#  string_to_goat_latin('Uber loves Goat Latin')
#
# would return: 'Ubermaa oveslmaaa oatGmaaaa atinLmaaaaa'

import re
import sys
import string

def string_to_goat_latin(sentence):
    
    #words = []
    #words = sentence.split(sentence)
    
    index = 0
    
    vowel_re = re.compile(r'^[aeiouAEIOU]')
    
    for word in sentence.split():
        
        if vowel_re.search(word):
            word = word + "ma"
            #print word
        else:
            word = word + word[0]
            word = word[1:]
            word = word + "ma"
                    
        index += 1
        
        for a_index in range(0, index):
            word = word + "a"
        
        print word,


def string_to_goat_latin_2(sentence):
    
    #words = []
    #words = sentence.split(sentence)
    
    index = 0
    
    #vowel_re = re.compile(r'^[aeiouAEIOU]')
    
    for word in sentence.split():
        
        if word[0] in ['a','e','i','o','u','A','E','I','O','U']:
            word = word + "ma"
            #print word
        else:
            word = word + word[0]
            word = word[1:]
            word = word + "ma"
                    
        index += 1
        
        #word = ((word + "a") for i in range(0, index))
        
        #for a_index in range(0, index):
        #    word = word + "a"
        
        print word + "a" * index,
        
                 
string_to_goat_latin("Uber loves Goat Latin")
