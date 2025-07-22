n = int(input()) 
a = sum(i for i in range(1, n) if n % i == 0)
if a == n:
    result = "Perfect"
elif a > n:
    result = "Abundant"
else:
    result = "Deficient"
print(f"The number {n} is {result}.")

for num in range(2, 501):
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        print(num)
        
s="Adithi,How are you?"
s2=s.split()
s="".join(s2)
print(s)

