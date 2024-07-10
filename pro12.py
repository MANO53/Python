import random
import string
numberes =[0,1,2,3,4,5,6,7,8,9]
random.shuffle(numberes)
print(numberes)
new_numberes=random.choices(numberes,k=2)
print(new_numberes)
random_5=random.choices(string.ascii_letters,k=5)
print(random_5)