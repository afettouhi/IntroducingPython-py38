# 3.1
years_list = [1976, 1977, 1978, 1979, 1980, 1981]

# 3.2
years_list[3]

# 3.3
years_list[5]

# 3.4
things = ["mozzarella", "cinderella", "salmonella"]

# 3.5
things[1].capitalize()
print(things)

# 3.6
things[0] = things[0].upper()
print(things)

# 3.7
del things[2]
print(things)

# 3.8
surprise = ["Groucho", "Chico", "Harpo"]

# 3.9
surprise[2] = surprise[2].lower()
surprise[2] = surprise[2][::-1]
surprise[2] = surprise[2].capitalize()
print(surprise)

# 3.10
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse',
}

# 3.11
print(e2f['walrus'])

# 3.12
f2e = dict((v, k) for k, v in e2f.items())

# 3.13
print(f2e['chien'])

# 3.14
set_e2f = set(e2f)
print(set_e2f)

# 3.15

animals = {'cats': ['Henri', 'Grumpy', 'Lucy'], 'octopi': '', 'emus': ''}
life = {'animals': animals, 'plants': '', 'other': ''}

# 3.16
print(life.keys())

# 3.17
print(life['animals'].keys())

# 3.18
print(life['animals']['cats'])
