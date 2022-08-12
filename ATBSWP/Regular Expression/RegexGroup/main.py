
import re

phoneRegex = re.compile(r'(\(\d\d\d\)) (\(\d\d\d\d-\d\d\d\d\))')
batmanRegex = re.compile(r'Bat(man|mobile|tery)')

phonemo = phoneRegex.findall("(415) (5555-5556) is my phone number.")

batMO= batmanRegex.findall("Batman has a Batmobil which runs on Batter.")


print(phonemo)
print(batMO)