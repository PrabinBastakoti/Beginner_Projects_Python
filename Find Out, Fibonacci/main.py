

def fibonacci_list(number):
    a= 0
    b = 1
    c = 0
    f_terms = [c]

    while a <= number:
        f_terms.append(c)
        c = a + b
        a = b
        b = c
    return f_terms

def is_fibonacci(user_input):
    if user_input in fibonacci_list(user_input):
        return True
    return False

def main():
    
    while True:
        try:
            user_input = int(input("Enter the number you want to check >>> "))
        except ValueError:
            print("Invalid input, Please Try again.\n")
            continue

        if is_fibonacci(user_input):
            print(f"{user_input} is a Fibonacci\n")
        else:
            print(f"{user_input} is not a Fibonacci\n")
    
if __name__ == '__main__':
    main()