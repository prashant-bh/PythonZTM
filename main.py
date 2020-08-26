basket= ['a', 'b', 'e','x', 'd']
basket.append('p')
new_basket= basket[:]
new_basket.sort()
print(basket)
print(new_basket)
basket.insert(1,'R')
basket.remove('d')
new_basket.pop()
basket.pop()
print(basket)
print(new_basket)