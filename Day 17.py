thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
thistuple = ("Python ",) * 3
print(thistuple)
thistuple = ("Python ") * 3
print(thistuple)
thistuple1 = (1, 2, 3, 4)
thistuple2 = (5, 6)
thistuple = thistuple1 + thistuple2
print(thistuple)
thistuple1 = (3, 4, 5, 6)
thistuple2 = thistuple1 + (1, 2, 3)
thistuple = thistuple1 + thistuple2
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
thislist = [3, 4, 5, 6, "A", "B"]
thistuple = tuple(thislist)
print(thistuple)
thislist = thistuple.index(5)
print(thislist)
x = thistuple.count("A")
print(x)
thistuple = (1, 2, 4, 8, 0, 5)
x = thistuple.index(8)
print(x)
x = thistuple.count(0)
print(x)
