
from nltk.util import ngrams
from nltk import word_tokenize
import random
txt='I am an NLPer'

ngram=ngrams(txt,2)
print(list(ngram))

word_gram=ngrams(word_tokenize(txt),2)
print(list(word_gram))



print('\n\n')
def char_ngram(text,n):
    # text=text.replace(' ','')
    grams=[text[i:i+n] for i in range(len(text)-n+1)]
    return grams
print(char_ngram('I am an NLPer',2))


def word_ngram(text,n):
    text=text.split(' ')
    grams=[text[i:i+n] for i in range(len(text)-n+1)]
    return grams

print(word_ngram('I am an NLPer',2))


def bigram_set():   #set {}, store multiple items, it is unordered, unindexed, no duplicates, unchangeable
    x=set(char_ngram('paraparaparadise',2))
    y=set(char_ngram('paragraph', 2))

    union=x.union(y)
    intersection=x.intersection(y)
    difference=union-intersection

    print('se' in x), print('se' in y)


    diff2=[b for b in x if b not in y]+[b for b in y if b not in x]
    return 0

print(bigram_set())




def cipherText(text):
    # to get ascii code use ord() function, chr returns string for unicode code
    cipheredText=''
    for c in text:
        if c.islower():
            cipheredText+=chr(219-ord(c))
        else:
            cipheredText+=c
    return cipheredText


print('cipher: ', cipherText('hello'), '\n decipher',cipherText(cipherText('hello')))

def typoglycemia(text):
    words=text.split(' ')
    output=[]
    for w in words:
        if len(w)<=4:
            output.append(w)
        else:
            to_shuffle=w[1:-1]
            new_w=w[0]+''.join(random.sample(to_shuffle, len(to_shuffle)))+w[-1]
            output.append(new_w)
    return ' '.join(output)
print(typoglycemia('I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind'))
