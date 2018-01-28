# encoding: utf-8
import nltk
from nltk.probability import FreqDist

#First part

grammar = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP | V NP NP | V
  PP -> P NP
  V -> "gives" | "sleeps" | "eats" | "finds"
  NP -> "Per" | "Kari" | "Ola" | "dinner" | "book" | Det N
  Det -> "a" | "the"
  N -> "book"
  P -> "to"
  """)

sentence = "Per gives a book to Kari".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tre in rd_parser.parse(sentence):
    print(tre)

sentence = "Kari gives Per the book".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tre in rd_parser.parse(sentence):
    print(tre)

sentence = "Ola sleeps".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tre in rd_parser.parse(sentence):
    print(tre)

sentence = "Kari eats".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tre in rd_parser.parse(sentence):
    print(tre)

sentence = "Kari eats dinner".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tre in rd_parser.parse(sentence):
    print(tre)

sentence = "Per finds the book".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tre in rd_parser.parse(sentence):
    print(tre)


grammar2 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> Vt NP | Vt NP PP | Vt NP NP | Vi
  PP -> P NP
  Vi -> "sleeps"| "eats"
  Vt -> "gives" | "eats" | "finds"
  NP -> "Per" | "Kari" | "Ola" | "dinner" | "book" | Det N
  Det -> "a" | "the"
  N -> "book"
  P -> "to"
  """)


sentence = "Kari sleeps the book".split()
rd_parser = nltk.RecursiveDescentParser(grammar2)
for tre in rd_parser.parse(sentence):
    print(tre)

sentence = "Ola finds".split()
rd_parser = nltk.RecursiveDescentParser(grammar2)
for tre in rd_parser.parse(sentence):
    print(tre)

#skrives ut ikke noe siden de er ikke lovlige sentenceer: ugrammatiske.


#Second part
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



print("The number of words in 'Removing' is",counter)


def sannsynlighet_gitt_removing(antall):
     return antall / counter


print("The probability for 'foam' giving 'removing' is:", sannsynlighet_gitt_removing(foam_antall))
print("The probability for 'breakfast' giving 'removing' is:", sannsynlighet_gitt_removing(breakfast_antall))
print("The probability for 'jam' giving 'removing' is:", sannsynlighet_gitt_removing(jam_antall))
print("The probability for 'paper' giving 'removing' is:", sannsynlighet_gitt_removing(paper_antall))
print("The probability for 'closely' giving 'removing' is:", sannsynlighet_gitt_removing(closely_antall))
print("The probability for 'day' giving 'removing' is:", sannsynlighet_gitt_removing(day_antall))
print("The probability for 'surface' giving 'removing' is:", sannsynlighet_gitt_removing(surface_antall))


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



print("Number of keys in 'selfmotion' is ",counter2)


def sannsynlighet_gitt_selfmotion(antall):
     return antall / counter2


print("The probability is:", sannsynlighet_gitt_selfmotion(across_antall))
print("The probability is:", sannsynlighet_gitt_selfmotion(lake_antall))
print("The probability is:", sannsynlighet_gitt_selfmotion(surface_antall))
print("The probability is:", sannsynlighet_gitt_selfmotion(day_antall))
print("The probability is:", sannsynlighet_gitt_selfmotion(low_antall))
print("The probability is:", sannsynlighet_gitt_selfmotion(road_antall))
print("The probability is:", sannsynlighet_gitt_selfmotion(light_antall))
print("The probability is:", sannsynlighet_gitt_selfmotion(towards_antall))
print("The probability is:", sannsynlighet_gitt_selfmotion(closely_antall))
print("The probability is:", sannsynlighet_gitt_selfmotion(tarmac_antall))
print("The probability is:", sannsynlighet_gitt_selfmotion(paper_antall))

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





print("The number of keys in 'reading' is ",counter3)


def sannsynlighet_gitt_reading(antall):
     return antall / counter3


print("The probability is:", sannsynlighet_gitt_reading(across_antall))
print("The probability is:", sannsynlighet_gitt_reading(novel_antall))
print("The probability is:", sannsynlighet_gitt_reading(glasses_antall))
print("The probability is:", sannsynlighet_gitt_reading(day_antall))
print("The probability is:", sannsynlighet_gitt_reading(low_antall))
print("The probability is:", sannsynlighet_gitt_reading(breakfast_antall))
print("The probability is:", sannsynlighet_gitt_reading(section_antall))
print("The probability is:", sannsynlighet_gitt_reading(tarmac_antall))
print("The probability is:", sannsynlighet_gitt_reading(paper_antall))
print("The probability is:", sannsynlighet_gitt_reading(book_antall))
print("The probability is:", sannsynlighet_gitt_reading(light_antall))

resultat = counter + counter2 + counter3
print(resultat)
print("The probability of 'Removing' is:", 2/16)
