# encoding: utf-8
import nltk
from nltk.probability import FreqDist


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
