
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D['food']) # Print key value = 'Spam'

D['quantity'] += 1 # Adds 1 to value of key 'quantity'
print(D)

# Mer normalt att lagra key:value-pairs allt eftersom.
D2 = {}
D2 ['name'] = 'Bob'
D2 ['job'] = 'Dev'
D2 ['age'] = 40

print(D2['name'])

# Man kan också göra dictionary på detta vis:
bob1 = dict(name='Bob', job='dev', age=40)
print(bob1)

# Nedan kallas zipping
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob2)

# Nesting, bra t.ex. när namn ska lagras med både för och efternamn, och flera titlar t.ex.

rec = {'name':{'first': 'Bob', 'last': 'Smith'}, 'jobs':['dev','mgr'], 'age': 40.5}
print(rec['name']['last']) # Print last name

print(rec['jobs']) # Print jobs
print(rec['jobs'][-1]) # Print last job
rec['jobs'].append('janitor') # Lägg till jobb
print(rec)

D = {'b': 2, 'a': 1,'c': 3}
print(D)
D['e'] = 99 # Lägga till key:value i en dict.
print(D)

# Hur vet man innan om en key inte finns?

print('f' in D) # Returns False

# IF/ELSE
if not 'c' in D:
    print('missing') # Kan printa missing om key inte finns i dict D.
else:
    print("Finns")
# GET
value = D.get('a', 0) # Get value av angiven key, default 0 om ej finns.
print(value)

# Samma funktion som Get ovan men if else:
value = D['a'] if 'a' in D else 0
print(value)

# for Loops
keys = list(D.keys()) # För att lagra alla keys i en lista callar vi dict.keys-funktion
print(keys)

keys.sort() # För att sedan sortera keys, då det inte går att sortera dict.
print(keys)

for x in keys:
    print(x, '=>', D[x])

# Ovan tre steg kan göras i nya sorted-funktionen - använd denna:

for key in sorted(D):
    print(key, '=>', D[key])

# for Loop fungerar på icke sequences också, t.ex. skriva varje bokstav i en string:

for c in 'spam':
    print(c)

# WHILE - loop

x = 4
while x > 0:
    print('spam!' * x)
    x -= 1 # Glöm ej -1, annars fortsätter denna oändligt

# Iterables

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares) # Upphöjt till två på tal ur listan och lagrar i listan squares

# Ovan kan också göras såhär, och är lättare att läsa - for loop:
squares = [] 
for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)

print(squares)

# TUPLES

T = (1, 2, 3, 4)
print(T)

T + (5, 6) # Concatenation
print(T[1:]) # Index + Slice

# Tuple-specifika methods
T.index(4)
T.count(4)

# För att ersätta ett värde i en tuple måste man gå omväg (immutable) - 
# t.ex. för att ersätta första värdet med 2:
T = (2,) + T[1:]
print(T)

for x in T:
    print("Hello")