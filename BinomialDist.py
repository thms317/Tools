import scipy.special as sp
import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)


print(nCr(121,0))
print(nCr(120,1))
print(nCr(119,2))
print(nCr(118,3))

print(sp.binom(121,0))
print(sp.binom(120,1))
print(sp.binom(119,2))
print(sp.binom(118,3))

print(sp.binom(121,0))
print(sp.binom(121,1))
print(sp.binom(121,2))
print(sp.binom(121,3))