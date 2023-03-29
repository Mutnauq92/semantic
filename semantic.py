import spacy
lan_model = input("Choose language model[sm | md] : ")

if lan_model == "sm":
    nlp = spacy.load('en_core_web_sm')
elif lan_model == "md":
    nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("CAT MONKEY BANANA")
print()
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# cat apple monkey banana
print("\nCat Apple Monkey Banana Tokens")
print()
tokens = nlp('cat apple monkey banana')

# created similarity for re-usability
def similarity_func(in_tokens):
    for token1 in in_tokens:
        for token2 in in_tokens:
            print(token1.text, token2.text, token1.similarity(token2))

similarity_func(tokens)
print()

"""
When using 'en_core_sm' model, there's a userwarning that,
the model in use does not have vectors, therefore may not
give useful similarity judgements.

It is clear that cat and banana have low similarity, because bananas are
least favourite food for cats

However, the relatioship between cat and monkey is highest since they are
both animals.

Moreover, bananas are monkeys favourite food, hence their similarity is higher
than that of monkey and apple or cat and banana or apple.

"""

print("OWN TOKENS : lion zebra cow grass tiger milk")
print()
# own tokens
own_tokens = nlp('lion zebra cow grass tiger milk')

similarity_func(own_tokens)

"""
When running the program with 'sm' language model, similarity between monkey and banana
decreased, and the similarity between cat and apple increased, which is not very accurate
since we know that, cats don't like fruits much and monkeys like bananas.

In my own example, the similarity between tiger and zebra is most notable.
see similarity comparison below.

tiger - zebra
'sm' model - 'md' model
0.1811...  - 1.0

The similarity difference is tremendous. The similarity is 1.0,
possibly because they are both mammals and have stripped fur coats.

"""
