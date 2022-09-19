from objects import File, Folder
from commands import *


root = Folder('', 'root')

a = Folder('a', 'root', root)
b = Folder('b', 'root', root)
c = File('c', 'root', root)

root.add_item(a, 'root')
root.add_item(b, 'root')
root.add_item(c, 'root')

'''
print(root.get_child(a))
for i in range(len(root.items)):
    print('root.items[i]', type(root.items[i]))
'''
