
import re
lyrics = '12 drummers drumming , 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, \
7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'
print("\n")
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))


print("\n")
vowelRegex = re.compile(r'[aeiouAEIOU]')  # r'(a|e|i|o|u) '
mo= vowelRegex.findall(lyrics)
print(mo)
print("\n")

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')  # r'(aa|ee|io|oi|ua) '
print(doubleVowelRegex.findall(lyrics))

print("\n")

consonants = re.compile(r'[^aeiouAEIOU]')  # ^ gives negative so negative of vowel consonants is displayed 
consonant= consonants.findall(lyrics)
print(consonant)
print("\n")