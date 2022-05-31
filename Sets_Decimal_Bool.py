
# Sets are unordered collections of unique and immutable objects

X = set('spam') # Gör set av sequence, s,p,a,m
print(X)

Y = {'h','a','m'} # Gör set av nämnda värden
print(Y)

print(X, Y) # Printa båda

print(X & Y) # Printa värden som finns i båda?

print(X|Y) # Ta bort dublettvärden

print(X - Y) # Difference?

print(X > Y)

print({n ** 2 for n in [1,2,3,4]})

# För att t.ex. filter out duplciates i lista

list(set([1,2,1,3,1]))

# Finding differences in collections
set('spam') - set('ham')

set('spam') == set('asmp') # True

# Kan iterate "in" också, för att se om värde finns i set.

'p' in set('spam') # = True

(2/3) + (1/2)

# Decimal = Fixed-precision float numbers.
import decimal
d = decimal.Decimal('3.141')
print(d)

1 > 2, 1 < 2    # False, True
bool('spam')    # Object's Boolean value, True

X = None        # Placeholder

L = [None] * 100 # Skapa lista av 100 namn, men värde None
print(L)


