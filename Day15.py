thislist = ["apple", "banana", "cherry"]
print(len(thislist))
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "apple", "cherry"]
thislist.remove("apple")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
thislist = ["Ahmad", "Omar", "Khalid"]
mylist = thislist
thislist.pop(0)
print(mylist)
print(thislist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
thislist = list(("apple", "banana", "cherry"))
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.reverse()
print(thislist)
thislist.append("orange")
print(thislist)
thislist.sort(reverse=False)
print(thislist)
