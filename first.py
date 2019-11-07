#!/usr/bin/python3

print("hello world")

a = 1
if  a  == 0:
	print ("toto")
else:
	print ("ne vaut pas 0")

print("fin")

"""
COMMENTAIRES

"""

sringadd = "aa" + "bb"
print(sringadd)

if a == 0:
	string =("coucou\n"
		 "salut\n"
		 "hello")
	print(string)
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"
if 'a' in alphabet:
	print("lettre trouvée")

alist = list()
alist = []
alist = ["a", "b"]
print(alist)
alist = range(5)
#liste de numéro de 0 à 5
print(alist)
for x in alist:
	print(x)

for char in alphabet:
	print(char, end="\n")
"""
#cherche tous les char de alphabet
"""
for st in alist:
	print(st)

#affiche le 3è élément
print(alist[3])

alist= []
#rajoute hello a alist
alist.append("hello")
print(alist)

#supprime un élément
alist.pop("a")
print(alist
"""

adict = dict()
adict = {}
adict = {"fr": "salut",
	 "en": "hello"}
print(adict)
print(adict["fr"])

"""
#ex
lang = "fr"
print(adict[lang])

#renvoie les clé dans adict
for key in adict:
	print(key)
	print(adict[key])

trad_fr {"bonjour": "salut",
	 "aie": "j'ai mal"}
trad_en {"bonjour": "hello",
	 "aie": "it hurts"}

lang = {"fr": "salut",
         "en": "hello"}
print(trad[lang]['aie'])
lang="en"
print(trad[lang]['aie'])
"""

#list
alist = ["0", "1", "2"]
list_comp = [x for x in alist]
list_comp = alist
print(list_comp)

list_comp = [x + "aa" for x in alist]
print(list_comp)

alist = ["fr", "en", "de"]
adict = {"fr": "salut",
         "en": "hello"}
adict = [key for key in adict]
print("je gere les langues", alist)
