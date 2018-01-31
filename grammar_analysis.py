# encoding: utf-8
import nltk

def parseExpression(expression):
    nodeMap = dict()
    counter = 1
    node = ""
    retExp =""
    i = 0

    for char in expression:
        if char == '(' or char == ')' :
            i+=1
            if (len(node) > 0):
                nodeMap[str(counter)] = node;
                retExp += str(counter)
                counter +=1
            retExp += char
            node =""
        elif char == ' ' and expression[i+1] == '(':
            i+=1
            continue
        else :
            i+=1
            node += char
    return retExp,nodeMap

def printTree(tree, node, nodeMap):
    if node not in tree:
        return
    print '%s -> %s' % (nodeMap[node], ' '.join(nodeMap[child] for child in tree[node]))

    for child in tree[node]:
        printTree(tree, child, nodeMap)

def toTree(expression):
    tree = dict()
    msg =""
    stack = list()
    for char in expression:
        if(char == '('):
            stack.append(msg)
            msg = ""
        elif char == ')':
            parent = stack.pop()
            if parent not in tree:
                tree[parent] = list()
            tree[parent].append(msg)
            msg = parent
        else:
            msg += char
    return tree


#grammar = nltk.CFG.fromstring("""
 #S -> NP VP
 #VP -> Vt NP | Vt NP PP | Vt NP NP | Vi
 #PP -> P NP
 #Vi -> "sleeps"| "eats"
 #Vt -> "gives" | "eats" | "finds"
 #NP -> "Per" | "Kari" | "Ola" | "dinner" | "book" | Det N
 #Det -> "a" | "the"
 #N -> "book"
 #P -> "to"
  #""")


grammar = nltk.data.load('my_grammar.cfg')

input_sentence = raw_input("Write a sentence: ")

sentence = input_sentence.split()
rd_parser = nltk.RecursiveDescentParser(grammar)

try:

    trees = rd_parser.parse(sentence)

    print("")
    print("The abreviations mean--> S: Sentence, NP: Noun phrase, VP: Verb phrase, AP: Adjective phrase")
    print("PP: Prepositional phrase, Adj: Adjective, Det: Determiner, V: Verb, N: Noun")
    print("")

    grammaticOk = 0;

    for t in trees:

        t, nodeMap = parseExpression(str(t))
        tree = toTree(t)
        printTree(tree, tree[''][0], nodeMap)
        grammaticOk = 1;
        break

    if grammaticOk == 0:

        print("That sentence is not grammatically correct")


except:

    print("Oops! That was not correctly spelled or outside my knowledge.")
