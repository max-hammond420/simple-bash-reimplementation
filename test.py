from objects import *
from exe_mkdir import mkdir

root = Folder('/', 'root')
#print(root.get_permissions())

new_folder = Folder('etc', 'root')
new_folder.add_parent_directory()
root.add_folder(new_folder)

print(root)
