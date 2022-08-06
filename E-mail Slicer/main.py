
def email_slicer():
    user_input = input("Enter your E-mail Address : ")
    username,_,domain = user_input.strip().partition('@')
    print(f"{username} is your Username and {domain} is the Domain.")
email_slicer()