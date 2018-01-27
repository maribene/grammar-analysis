# encoding: utf-8
import nltk
from nltk.probability import FreqDist

#oppgave 1

grammatikk = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP | V NP NP | V
  PP -> P NP
  V -> "gir" | "sover" | "spiser" | "finner"
  NP -> "Per" | "Kari" | "Ola" | "middag" | "boka" | Det N
  Det -> "en"
  N -> "bok"
  P -> "til"
  """)

setning = "Per gir en bok til Kari".split()
rd_parser = nltk.RecursiveDescentParser(grammatikk)
for tre in rd_parser.parse(setning):
    print(tre)

setning = "Kari gir Per boka".split()
rd_parser = nltk.RecursiveDescentParser(grammatikk)
for tre in rd_parser.parse(setning):
    print(tre)

setning = "Ola sover".split()
rd_parser = nltk.RecursiveDescentParser(grammatikk)
for tre in rd_parser.parse(setning):
    print(tre)

setning = "Kari spiser".split()
rd_parser = nltk.RecursiveDescentParser(grammatikk)
for tre in rd_parser.parse(setning):
    print(tre)

setning = "Kari spiser middag".split()
rd_parser = nltk.RecursiveDescentParser(grammatikk)
for tre in rd_parser.parse(setning):
    print(tre)

setning = "Per finner boka".split()
rd_parser = nltk.RecursiveDescentParser(grammatikk)
for tre in rd_parser.parse(setning):
    print(tre)

"""
(S
  (NP Per)
  (VP (V gir) (NP (Det en) (N bok)) (PP (P til) (NP Kari))))
(S (NP Kari) (VP (V gir) (NP Per) (NP boka)))
(S (NP Ola) (VP (V sover)))
(S (NP Kari) (VP (V spiser)))
(S (NP Kari) (VP (V spiser) (NP middag)))
(S (NP Per) (VP (V finner) (NP boka)))
"""
"""
setning = "Kari sover boka".split()
rd_parser = nltk.RecursiveDescentParser(grammatikk)
for tre in rd_parser.parse(setning):
    print(tre)
setning = "Ola finner".split()
rd_parser = nltk.RecursiveDescentParser(grammatikk)
for tre in rd_parser.parse(setning):
    print(tre)

(S (NP Kari) (VP (V sover) (NP boka)))
(S (NP Ola) (VP (V finner)))

"""
grammatikk2 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> Vt NP | Vt NP PP | Vt NP NP | Vi
  PP -> P NP
  Vi -> "sover"| "spiser"
  Vt -> "gir" | "spiser" | "finner"
  NP -> "Per" | "Kari" | "Ola" | "middag" | "boka" | Det N
  Det -> "en"
  N -> "bok"
  P -> "til"
  """)


setning = "Kari sover boka".split()
rd_parser = nltk.RecursiveDescentParser(grammatikk2)
for tre in rd_parser.parse(setning):
    print(tre)

setning = "Ola finner".split()
rd_parser = nltk.RecursiveDescentParser(grammatikk2)
for tre in rd_parser.parse(setning):
    print(tre)

#skrives ut ikke noe siden de er ikke lovlige setninger: ugrammatiske.


#oppgave 2

 #setning 1. : verb leave 7
 #setning 2. : verb leave 11
 #setning 3. : verb leave 8
 #setning 4. : verb leave 5
 #setning 5. : verb leave 13

#setning 13 var veldig vaskelig å forstå hva de menteself.

#oppgave 3
from collections import defaultdict

d = defaultdict(list)

liste = []
fil = open("wsd_tren.txt")



for line in fil:
    liste.append(line[0:])

for elem in liste:
    elem = elem.rstrip("\n")
    a = elem.split(" ")
    d[a[0]].append(a[1:])


print("Removing keys:", d["Removing"], "\n")
print("Self-motion keys:", d["Self_motion"], "\n")
print("Reading keys:", d["Reading"], "\n")

counter = 0
liste = []

for elem in d["Removing"]:
    for i in elem:
        counter+=1
        liste.append(i)


foam_antall = liste.count("foam")
breakfast_antall = liste.count("breakfast")
jam_antall = liste.count("jam")
paper_antall = liste.count("paper")
closely_antall = liste.count("closely")
day_antall = liste.count("day")
surface_antall = liste.count("surface")



print("Antall keys i removing er ",counter)


def sannsynlighet_gitt_removing(antall):
     return antall / counter


print("Sannsynligheten av foam gitt removing er:", sannsynlighet_gitt_removing(foam_antall))
print("Sannsynligheten av breakfast gitt removing er:", sannsynlighet_gitt_removing(breakfast_antall))
print("Sannsynligheten av jam gitt removing er:", sannsynlighet_gitt_removing(jam_antall))
print("Sannsynligheten av paper gitt removing er:", sannsynlighet_gitt_removing(paper_antall))
print("Sannsynligheten av closely gitt removing er:", sannsynlighet_gitt_removing(closely_antall))
print("Sannsynligheten av day gitt removing er:", sannsynlighet_gitt_removing(day_antall))
print("Sannsynligheten av surface gitt removing er:", sannsynlighet_gitt_removing(surface_antall))


counter2 = 0
liste = []

for elem in d["Self_motion"]:
    for i in elem:
        counter2+=1
        liste.append(i)


across_antall = liste.count("across")
lake_antall = liste.count("lake")
surface_antall = liste.count("surface")
day_antall = liste.count("day")
low_antall = liste.count("low")
road_antall = liste.count("road")
light_antall = liste.count("light")
towards_antall = liste.count("towards")
closely_antall = liste.count("closely")
tarmac_antall = liste.count("tarmac")
paper_antall = liste.count("paper")



print("Antall keys i selfmotion er ",counter2)


def sannsynlighet_gitt_selfmotion(antall):
     return antall / counter2


print("Sannsynligheten er:", sannsynlighet_gitt_selfmotion(across_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_selfmotion(lake_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_selfmotion(surface_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_selfmotion(day_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_selfmotion(low_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_selfmotion(road_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_selfmotion(light_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_selfmotion(towards_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_selfmotion(closely_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_selfmotion(tarmac_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_selfmotion(paper_antall))

counter3 = 0
liste = []

for elem in d["Reading"]:
    for i in elem:
        counter3+=1
        liste.append(i)

tarmac_antall = liste.count("tarmac")
section_antall = liste.count("section")
paper_antall = liste.count("paper")
day_antall = liste.count("day")
book_antall = liste.count("book")
novel_antall = liste.count("novel")
breakfast_antall = liste.count("breakfast")
low_antall = liste.count("low")
light_antall = liste.count("light")
across_antall = liste.count("across")
glasses_antall = liste.count("glasses")





print("Antall keys i reading er ",counter3)


def sannsynlighet_gitt_reading(antall):
     return antall / counter3


print("Sannsynligheten er:", sannsynlighet_gitt_reading(across_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_reading(novel_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_reading(glasses_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_reading(day_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_reading(low_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_reading(breakfast_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_reading(section_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_reading(tarmac_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_reading(paper_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_reading(book_antall))
print("Sannsynligheten er:", sannsynlighet_gitt_reading(light_antall))

resultat = counter + counter2 + counter3
print(resultat)
print("Sannsynlighet av Removing er:", 2/16)
