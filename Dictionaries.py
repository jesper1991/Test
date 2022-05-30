
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
rec['jobs'].append('janitor') # L'gg till jobb
print(rec)