class File():
    # group owner, permissions
    def __init__(self, name, owner):
        #super().__init__(self, name, user)

        self.name = name
        self.owner = owner

        # Read, Write, Execute
        self.owner_permissions = [True, True, False]
        self.other_permissions = [True, False, False]

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_permissions(self) -> str:
        owner_str = ''
        other_str = ''
        perms = ['r', 'w', 'x']
        for i in range(len(self.owner_permissions)):
            if self.owner_permissions[i]:
                owner_str += perms[i]
            else:
                owner_str += '-'
        for i in range(len(self.other_permissions)):
            if self.other_permissions[i]:
                other_str += perms[i]
            else:
                other_str += '-'
        return '-' + owner_str + other_str

    def check_modify_permissions(self) -> bool:
        # returns True if current user is able to modify the file
        pass

    def chmod(self, modify_string):
        pass


class Folder():
    # contains links to more items
    def __init__(self, name, owner, parent=None):

        self.items = []
        self.parent = None

        self.name = name+"/"
        self.owner = owner

        # Read, Write, Execute
        self.owner_permissions = [True, True, True]
        self.other_permissions = [True, False, True]

    def __str__(self):
        #return str(self.__class__) + ": " + str(self.__dict__)
        return self.name

    def get_parent(self):
        return self.parent

    def get_name(self) -> str:
        return self.name

    def get_items(self) -> list:
        return self.items

    def get_permissions(self) -> str:
        owner_str = ''
        other_str = ''
        perms = ['r', 'w', 'x']
        for i in range(len(self.owner_permissions)):
            if self.owner_permissions[i]:
                owner_str += perms[i]
            else:
                owner_str += '-'
        for i in range(len(self.other_permissions)):
            if self.other_permissions[i]:
                other_str += perms[i]
            else:
                other_str += '-'

        return 'd' + owner_str + other_str

    def add_item(self, name, user):
        # add children
        self.items.append(name)

    def add_parent_directory(self) -> None:
        # only use if folder is not root
        self.items.append('.')
        self.items.append('..')

    def add_parent(self, parent):
        self.parent = parent

def get_every_folder(s):
    # takes in string /a/b/c -> ['', 'a', 'b', 'c']
    # or a/b/c -> ['a', 'b', 'c']
    s = s.split('/')
    return s

def cd(name, user, parent_folder, root):
    if name == '.':
        return parent_folder
    elif name == '..':
        if parent_folder.parent == None:
            return root
        return parent_folder.parent
    if name == '':
        return root
    name += '/'
    for folder in parent_folder.get_items():
        if folder.get_name() == name:
            if type(folder) == Folder:
                return folder
            elif type(folder) == File:
                print("cd: Destination is a file")
                return parent_folder
    print("cd: No such file or directory")
    return parent_folder

def ls(folder):
    for item in folder.get_items():
        print(item)

def mkdir(cwd, user, parent_folders):
    if parent_folders[0] == '':
        parent_folders = parent_folders[1:]
    new_folder_name = parent_folders[-1]
    if len(parent_folders) > 1:
        parent_folders = parent_folders[:-1]
        for i in range(len(parent_folders)):
            cwd_items = []
            for j in range(len(cwd.get_items())):
                cwd_items.append(cwd.get_items()[j].get_name()[:-1])
            if parent_folders[i] in cwd_items:
                index = cwd_items.index(parent_folders[i])
                cwd = cwd.get_items()[index]
            else:
                print("mkdir: Ancestor directory does not exist")
                return None
    else:
        parent_folders = [cwd]
    #print(new_folder_name, parent_folders)
    new_folder = Folder(new_folder_name, user, cwd)
    #print(parent_folders[-1])
    #print(cwd)
    new_folder.add_parent(cwd)
    return cwd.add_item(new_folder, user)

def mkdir_dashp(cwd, user, parent_folders):
    # iterate over parent_folders,
    # check when cwd is does not exist, and mkdir on that
    if parent_folders[0] == '':
        parent_folders = parent_folders[1:]
    existing_folders = []
    tbc_folders = []
    for i in range(len(parent_folders)):
        pass

def touch(parent_folder, name, user):
    new_file = File(name, user)
    parent_folder.add_item(new_file, user)

def pwd(current_directory):
    ls = [current_directory]
    while current_directory.get_parent() != None:
        ls.append(current_directory.get_parent())
        current_directory = current_directory.get_parent()

    s = ''
    ls_size = len(ls)
    for i in range(len(ls)-1, -1, -1):
        s += ls[i].get_name()
    return s

def ls(current_directory):
    s = ''
    for item in current_directory.get_items():
        if type(item) == Folder:
            s += (item.get_name()[:-1] + ' ')
        else:
            s += (item.get_name() + ' ')

    return s
