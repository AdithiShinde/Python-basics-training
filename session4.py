l = list(map(int, input("Enter numbers separated by space: ").split()))
print(l)

x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

s = "As Soon As Possible"
S1 = ""
for i in range(len(s)):
    if i == 0 or s[i - 1] == " ":
        S1 += s[i]
print(S1)

s = "As Soon As Possible"
l = s.split()
a = ""
for i in l:
    a = a + i[0]
print(a.upper())

x = 56.893421
print(f"{x:0>8.2f}")
print(f"{x:0<9.2f}")
print(f"{x:0^9.2f}")

y = 4
print(f"{y:+>5.2f}")

l = [1, 2, 7, 4, "ds", "da", 6.4]
for i in l:
    print(i)

V = list(map(int, input("Enter a list of numbers: ").split()))
P = [x // 2 if i % 2 != 0 else x ** 2 for i, x in enumerate(V)]
print(P)

L = [1, 2, 3, 4, 5, 6, 7, 8]
first_half = L[:4]
second_half = L[4:]
reversed_list = L[::-1]
even_indices = L[::3]
odd_indices = L[1::2]
print("First half:", first_half)
print("Second half:", second_half)
print("Reversed list:", reversed_list)
print("Even indices:", even_indices)
print("Odd indices:", odd_indices)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = [x for x in l if x % 2 == 0]
print(l)

s = input("Enter a string: ").lower()
a = "abcdefghijklmnopqrstuvwxyz"
for i in a:
    if i not in s:
        print("Not a pangram")
        break
else:
    print("Pangram")

def vowelcount(s):
    return len([i for i in s.lower() if i in "aeiou"])

def Sum(s):
    return sum([ord(i) for i in s])

l = ["Siri", "Meghana", "Senorita", "Aryan"]
l.sort(key=vowelcount)
l.sort(key=Sum)
print(l)
