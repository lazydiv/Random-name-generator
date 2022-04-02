from os import write
from random import randint
from name_list import name_list


f = open("names.txt", mode="w")



for x in range(50000):
    first_random_number = randint(0, len(name_list))
    last_random_number = randint(0, len(name_list))

    f.write("\n" + name_list[first_random_number - 1] + " " + name_list[last_random_number - 1])

f.close