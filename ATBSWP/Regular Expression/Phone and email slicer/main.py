
import re
import pyperclip


# create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\))) ?      # area code(optional)
(\s|-)                           # first separator
\d\d\d                           # first 3 digits
-                                # separator
\d\d\d\d                         # last 4 digits
(((ext(\.)?\s)|x)                # extension word-part (optional)
 (\d{2,5}))?                     # extension number-part(optional)
)
''',re.VERBOSE)

# create a regex for email addresses
emailRegex = re.compile(r'''

#some.+_thing@somthing.com#

[a-zA-Z0-9_.+]+                                #name part 
@                                #@ symbol
[a-zA-Z0-9_.+]+                                # domain name part

''',re.VERBOSE)

# Get the text off the clipboard

text = pyperclip.paste()

# Extract the email/phone from this text

extracted_phone = phoneRegex.findall(text)

extracted_email = emailRegex.findall(text)

allphoneNumbers = []
for phoneNumber in extracted_phone:
    allphoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard

results ='\n'.join(allphoneNumbers) + '\n' + '\n'.join(extracted_email)

pyperclip.copy(results)

