n=12
if n%2==0:
    print("Even")
    print("Odd")
else:
    print(z)
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"leap year.")
else:
    print(f"not a leap year.")
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)
a = int(input())
b = int(input())
c = int(input())
if a + b >= c and b + c >= a and c + a >= b:
    print("Can form a triangle.")
else:
    print("Cannot form a triangle.")

n = int(input("Enter a positive integer: "))
steps = 0

if n > 0:
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    print(f"Number of steps to reach 1: {steps}")
else:
    print("Please enter a positive integer.")
    
n = int(input("Enter a number: "))
sum_of_digits = 0
while n > 0:
    sum_of_digits += n % 10 
    n //= 10  
print("Sum of all digits:", sum_of_digits)

n=24231
count=0
while(n!=0):
    n=n//10
    count+=1
print(count)

num = int(input("Enter a number: "))
n = len(str(num))
temp = num
armstrong_sum = 0
while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** n
    temp //= 10
if armstrong_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
