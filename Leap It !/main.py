
import time
time.sleep(0.5)
while True:


    try:
        user_year = int(input("\nEnter the year > "))

    except ValueError:
        print("Invalid input. Only integers is allowed\n")
        exit()

    if (user_year % 100 == 0) and (user_year % 400 == 0 ):
            print(f"The year {user_year} is a leap year(It has 366 days).\n")
            time.sleep(1.5)

    elif (user_year % 4 ==  0) and (user_year %100 !=0) :
        print(f"The year {user_year} is a leap year(It has 366 days).\n")
        time.sleep(1.5)
        

    else:
        print(f"The year {user_year} is not a leap year (It has 365 days).\n")
        time.sleep(1.5)