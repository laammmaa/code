thisset = {"apple", "banana", "cherry"}
print(len(thisset))
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
thisset = set(("apple", "banana", "cherry"))
print(thisset)