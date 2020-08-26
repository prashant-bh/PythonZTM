basket= ['a', 'b', 'e','x', 'd']
new_basket=basket[:]
basket.extend('C')
new_basket=basket.clear()
print(basket)
print(new_basket)