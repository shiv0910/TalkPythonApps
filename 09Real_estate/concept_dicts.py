

lookup = {}
lookup = dict()
lookup = {'age': 42, 'loc': 'Italy'}
lookup = dict(age=42, loc='Italy')

class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.name = name

gandalf = Wizard("Gandalf", 42)
print(gandalf.__dict__)

print(lookup)
print(lookup['loc'])

lookup['cat'] = 'Fun code demos'

if 'cat' in lookup:
    print(lookup['cat'])

import collections

user = collections.namedtuple('User', 'id, name, email')
users = [
    user(1, 'user1', 'user1@yahoo.com'),
    user(2, 'user2', 'user2@yahoo.com'),
    user(3, 'user3', 'user3@yahoo.com'),
    user(4, 'user4', 'user4@yahoo.com'),
    user(5, 'user5', 'user5@yahoo.com')
]

lookup = dict()
for u in users:
    lookup[u.id] = u

print(lookup[4])

    # can change to [u.email] etc
    # lookup[u.email] = u
    # print(lookup['user4@yahoo.com'])

