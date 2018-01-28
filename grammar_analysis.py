# encoding: utf-8
import nltk
from nltk.probability import FreqDist


grammar = nltk.CFG.fromstring("""
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

input_sentence = raw_input("Write a sentence: ")

sentence = input_sentence.split()
rd_parser = nltk.RecursiveDescentParser(grammar)
trees = rd_parser.parse(sentence)

for tree in trees:
    print(tree)

"""
"Per gives a book to Kari"
"Kari gives Per the book"
"Ola sleeps"
"Kari eats"
"Kari eats dinner"
"Per finds the book"

---not grammatically correct

"Kari sleeps the book"
"Ola finds"
"""
