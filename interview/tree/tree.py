from collections import defaultdict
import json

def tree():
    return defaultdict(tree)

users = tree()
users['codingpy']['username'] = 'earlgery'
users['python']['username'] = 'Guido van Rossum'
print(json.dumps(users))

categories = tree()
categories['Programming Languages']['Python']
categories['Python']['Standard Library']['sys']
categories['Python']['Standard Library']['os']
print(json.dumps(categories))