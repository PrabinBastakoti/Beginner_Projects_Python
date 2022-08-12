
import re

beginswithHelloRegex = re.compile (r'^Hello') #Hello should be at the very begining of the string.
endswithWorldRegex = re.compile (r'World!$') #World! should be at the very end of the string.
print("\n")
print(beginswithHelloRegex.search("Hello There!"))
print("\n")
print(endswithWorldRegex.search("Hello World!"))

print("\n")
alldigitsregex = re.compile(r'^\d+$')
print(alldigitsregex.search("29642642764872846294629472"))
print("\n")
print(alldigitsregex.search("2964264276487x846294629472"))
print("\n")
atRegex = re.compile(r'.at') #anything followed by at
print(atRegex.findall("The cat in the hat sat on the flat mat."))
print("\n")
atRegex = re.compile(r'.{1,2}at') #anything followed by at
print(atRegex.findall("The cat in the hat sat on the flat mat."))
print("\n")
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Prabin Last Name: Bastakoti'))
print("\n")
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))
print("\n")
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))
print("\n")
prime ='Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)
print("\n")
dotstar = re.compile(r'.*')
print(dotstar.search(prime))
print("\n")
dotstar = re.compile(r'.*', re.DOTALL)
print(dotstar.search(prime))
print("\n")
vowelRegex = re.compile(r'[aeiou]',re.I) # Matches every case word. Ignore lower or upper case and displays all characters.
print(vowelRegex.findall('Al, why does your programming book talk about Robocap so much? '))
print("\n")