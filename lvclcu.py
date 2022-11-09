#<span style="color: #000000;">#https://cbsepython.in
from string import ascii_lowercase
import random
import time

name1 = input("Please type Your Name >\n")
name2 = input("Please type Your Crush Name >\n")

vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = set(ascii_lowercase) ^ vowels

def count_vowels(name):
    count = 0
    for i in vowels:
        count += name2.count(i)

    return count

total_vowel1 = count_vowels(name1)
total_vowel2 = count_vowels(name2)

love = 0
if(total_vowel1 == total_vowel2):
    love += random.randint(10, 30)

consonants1 = len([letter for letter in name1 if letter.lower() in consonants])
consonants2 = len([letter for letter in name2 if letter.lower() in consonants])

if(consonants1 == consonants2):
    love += random.randint(20, 40)

line1 = name1
line2 = name2
split1 = line1.split()
split2 = line2.split()
fl1 = [word[0] for word in split1]
fl2 = [word[0] for word in split2]

if (fl1 == fl2):
    love += random.randint(10,30)

if (len(name1) == len(name2)):
    love += random.randint(1,10)

love += random.randint(10,50)

if (love > 100):
    love = 100

print("Calculating...")

print(name1, "and", name2, "have a", love, "% relationship.")

if love >= 90:
    print("You have an unbreakable relationship that will last forever")

elif 70 <= love <= 89:
    print("You have a strong relationship that will most likely lead to a marriage.")

elif 50 <= love <= 69:
    print("You have a good relationship that can lead to a honeymoon to Paris.")

else:
    print("You have a weak relationship that could have been a 'match made in heaven'.")
#</span>
