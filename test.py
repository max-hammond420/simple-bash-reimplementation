from objects import *
from exe_mkdir import mkdir

root = Folder('/', 'root')
#print(root.get_permissions())

root.add_folder('new_folder', 'root')

mkdir(root, ['mkdir', 'new_folder2'], 'root')

print(root)

