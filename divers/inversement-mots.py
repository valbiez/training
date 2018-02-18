#!/usr/bin/env python
# -*- coding: utf-8 -*-

def inversemot(mot):
    resultat = ''
    u = len(mot)
    for k in range(u):
        resultat = resultat + mot[u-k-1]
    return resultat

#phrase = ' Bonjour ami : viens me voir a la maison.'
phrase = raw_input("> ")

phrase_inversee = ''

mots=phrase.lower().split(' ')
print mots

for k in range(len(mots)):
    mots[k] = inversemot(mots[k])
    phrase_inversee = phrase_inversee + mots[k] + ' '

phrase_inversee = phrase_inversee[0:len(phrase_inversee)-1]
#print mots
print repr(phrase_inversee)
