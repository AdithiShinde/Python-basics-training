s = {"apple", "mango", "pineapple", "orange"}
s.add("grapes")
s.remove("apple")
print(s.pop())
s.clear()
del s

s2 = {"sru"}

s = [2, 4, 5, 6, 8, 3, 5, 2, 1, 6, 7, 9, 6, 2, 4, 6]
t = set()
repeated_elements = set(x for x in s if x in t or t.add(x))
print(list(repeated_elements))

s1 = {"apple", "mango", "pineapple", "orange"}
s2 = {"mango", "guava", "grapes"}
print(s1.union(s2))
print(s1 | s2)
print(s1.intersection(s2))
print(s1 & s2)
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

s = "abcdef"
if len(s) == len(set(s)):
    print("Heterogram")
else:
    print("Not a Heterogram")

l1 = {3, 7, 8, 12, 6, 9}
l2 = {9, 12, 8}
print(l2.issubset(l1))
print(l1.issuperset(l2))
print(l1.isdisjoint(l2))

for i in l1:
    if i in set(l2):
        print(i)
print([i for i in l1 if i in set(l2)])

d = {
    'name': "Adithi Shinde",
    'Clg': "SRU",
    'Mobile': 9533330028,
    "CGPA": 9.1,
}
print(d["name"])
d["Clg"] = "MVGR"
print()
print(d)
print(d.items())
print(d.keys())
print(d.values())

del d["Mobile"]
print(d)

d.setdefault("clg", "MVGR")
d.setdefault("backlogs", 0)

l = [1, 2, 7, 4, 5, 4, 7, 8, 9, 5]
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)

s1 = "master"
s2 = "stream"
d1, d2 = {}, {}
for i in s1:
    if i not in d1:
        d1[i] = 1
    else:
        d1[i] += 1
for i in s2:
    if i not in d2:
        d2[i] = 1
    else:
        d2[i] += 1
print(d1 == d2)

from collections import Counter
s1 = "master"
s2 = "stream"
print(Counter(s1) == Counter(s2))
