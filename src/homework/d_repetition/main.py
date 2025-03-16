def get_factorial(num):
    factorial = 1 
    for i in range (1, num + 1):
        #factorial *= i
        factorial = factorial * i
    return factorial

def sum_odd_numbers(num):
    total = 0 
    i = 1
    while i <= num:
        total += i
        i += 2
    return total

def menu():
    while True:
        print ("Homework 3 menu")
        print ("1 - Factorial")
        print ("2 - Sum Odd Numbers")
        print ("3 - Exit ")
        
        number = input ("select a number")
        if number == "1":
            while True:
                number = int(input("pick a number from 1-9:"))
                if 0 < number < 10:
                    print(f"the factorial of {number} is {get_factorial(number)}")
                    break
                else:
                    print("The Number needs to be between 1-9")
        elif number == "2":
            while True:
                number = int(input("Enter number between 1-99:"))
                if 0 < number < 100:
                    print(f"The sum of odd numbers up to {number}is {sum_odd_numbers(number)}")
                    break
                else:
                    print("choose a different number thats under 99")
        elif number == "3":
            Exit = input("do you want to exit? yes or no")
            if Exit == "yes":
                print("Goodbye")
                break
            else:
                continue
menu()