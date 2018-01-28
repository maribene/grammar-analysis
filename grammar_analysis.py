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
for tree in rd_parser.parse(sentence):
    print(tree)

sentence = "Kari gives Per the book".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tree in rd_parser.parse(sentence):
    print(tree)

sentence = "Ola sleeps".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tree in rd_parser.parse(sentence):
    print(tree)

sentence = "Kari eats".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tree in rd_parser.parse(sentence):
    print(tree)

sentence = "Kari eats dinner".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tree in rd_parser.parse(sentence):
    print(tree)

sentence = "Per finds the book".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tree in rd_parser.parse(sentence):
    print(tree)


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
for tree in rd_parser.parse(sentence):
    print(tree)

sentence = "Ola finds".split()
rd_parser = nltk.RecursiveDescentParser(grammar2)
for tree in rd_parser.parse(sentence):
    print(tree)

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


foam_nr = liste.count("foam")
breakfast_nr = liste.count("breakfast")
jam_nr = liste.count("jam")
paper_nr = liste.count("paper")
closely_nr = liste.count("closely")
day_nr = liste.count("day")
surface_nr = liste.count("surface")



print("The number of words in 'Removing' is",counter)


def sannsynlighet_gitt_removing(nr):
     return nr / counter


print("The probability for 'foam' giving 'removing' is:", sannsynlighet_gitt_removing(foam_nr))
print("The probability for 'breakfast' giving 'removing' is:", sannsynlighet_gitt_removing(breakfast_nr))
print("The probability for 'jam' giving 'removing' is:", sannsynlighet_gitt_removing(jam_nr))
print("The probability for 'paper' giving 'removing' is:", sannsynlighet_gitt_removing(paper_nr))
print("The probability for 'closely' giving 'removing' is:", sannsynlighet_gitt_removing(closely_nr))
print("The probability for 'day' giving 'removing' is:", sannsynlighet_gitt_removing(day_nr))
print("The probability for 'surface' giving 'removing' is:", sannsynlighet_gitt_removing(surface_nr))


counter2 = 0
liste = []

for elem in d["Self_motion"]:
    for i in elem:
        counter2+=1
        liste.append(i)


across_nr = liste.count("across")
lake_nr = liste.count("lake")
surface_nr = liste.count("surface")
day_nr = liste.count("day")
low_nr = liste.count("low")
road_nr = liste.count("road")
light_nr = liste.count("light")
towards_nr = liste.count("towards")
closely_nr = liste.count("closely")
tarmac_nr = liste.count("tarmac")
paper_nr = liste.count("paper")



print("Number of keys in 'selfmotion' is ",counter2)


def probability_giving_selfmotion(nr):
     return nr / counter2


print("The probability is:", probability_giving_selfmotion(across_nr))
print("The probability is:", probability_giving_selfmotion(lake_nr))
print("The probability is:", probability_giving_selfmotion(surface_nr))
print("The probability is:", probability_giving_selfmotion(day_nr))
print("The probability is:", probability_giving_selfmotion(low_nr))
print("The probability is:", probability_giving_selfmotion(road_nr))
print("The probability is:", probability_giving_selfmotion(light_nr))
print("The probability is:", probability_giving_selfmotion(towards_nr))
print("The probability is:", probability_giving_selfmotion(closely_nr))
print("The probability is:", probability_giving_selfmotion(tarmac_nr))
print("The probability is:", probability_giving_selfmotion(paper_nr))

counter3 = 0
liste = []

for elem in d["Reading"]:
    for i in elem:
        counter3+=1
        liste.append(i)

tarmac_nr = liste.count("tarmac")
section_nr = liste.count("section")
paper_nr = liste.count("paper")
day_nr = liste.count("day")
book_nr = liste.count("book")
novel_nr = liste.count("novel")
breakfast_nr = liste.count("breakfast")
low_nr = liste.count("low")
light_nr = liste.count("light")
across_nr = liste.count("across")
glasses_nr = liste.count("glasses")





print("The number of keys in 'reading' is ",counter3)


def probability_giving_reading(nr):
     return nr / counter3


print("The probability is:", probability_giving_reading(across_nr))
print("The probability is:", probability_giving_reading(novel_nr))
print("The probability is:", probability_giving_reading(glasses_nr))
print("The probability is:", probability_giving_reading(day_nr))
print("The probability is:", probability_giving_reading(low_nr))
print("The probability is:", probability_giving_reading(breakfast_nr))
print("The probability is:", probability_giving_reading(section_nr))
print("The probability is:", probability_giving_reading(tarmac_nr))
print("The probability is:", probability_giving_reading(paper_nr))
print("The probability is:", probability_giving_reading(book_nr))
print("The probability is:", probability_giving_reading(light_nr))

resultat = counter + counter2 + counter3
print(resultat)
print("The probability of 'Removing' is:", 2/16)
