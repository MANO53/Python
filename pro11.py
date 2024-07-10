import string
sentence=input(" please enter a sentence ")
new_sentence=""
for i in sentence:
    if i not in string.punctuation:
        new_sentence+=i
print(f"\n\n*******here the same sentence *******\n\n   {new_sentence}")