
#Task 1: Calculate Factorial Using a Function

def factorial_num(num):
    factorial=1
    for i in range(1,num+1):
        factorial=i*factorial
    return factorial


num=int(input("Enter a number: "))
factorial_num(num)
print(f"Factorial of {num} is: {factorial_num(num)}")

