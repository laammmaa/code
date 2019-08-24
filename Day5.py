x = 'Apple'
y = ' Orange'
z = ' limon'
Basket = x + y + z
print(Basket)
print(Basket.split())
n = 6
print([Basket[i:i + n] for i in range(0, len(Basket), n)])
