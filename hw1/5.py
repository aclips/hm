from scipy.misc import factorial

def _diff(n):
    _n = n - 1
    return (n/factorial(n)**(1/n)) - (_n/factorial(_n)**(1/_n))

accuracy = 0.0000001
i = 2
step = 1

while  _diff(i) > accuracy:
    i = i + step
    
print(i)
