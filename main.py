basket= ['a', 'b', 'e','x', 'd']
basket.append('p')
new_basket= basket[:]
new_basket.sort()
basket.insert(1,'R')
basket.remove('d')
print(basket)
print(new_basket)