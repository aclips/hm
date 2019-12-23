a = set('13579')
b = set('24569')
c = {()}

print(a.union(b))
#{'9', '5', '4', '3', '2', '7', '6', '1'}

print(a.intersection(b))
#{'9', '5'}

print(a.difference(b))
#{'7', '3', '1'}

print(b.difference(a))
#{'2', '6', '4'}

print(a.symmetric_difference(b))
#{'4', '3', '2', '7', '6', '1'}

print(a.union(c))
#{'9', '3', (), '5', '7', '1'}

print(a.intersection(c))
#{}

print(a.difference(c))
#{'7', '3', '9', '5', '1'}

print(c.difference(a))
#{}

print(a.symmetric_difference(c))
#{'9', '5', (), '3', '7', '1'}
