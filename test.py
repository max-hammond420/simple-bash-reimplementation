from objects import *

root = Folder('', 'root')
mkdir(['mkdir', 'folder1'], 'root', root)
mkdir(['mkdir', 'folder2'], 'root', root)


cwd = cd('folder1', 'root', root)

print(cwd)
print(pwd(cwd))
print(ls(cwd))
#print()
#print(ls(root))
#print()
#print(root)
