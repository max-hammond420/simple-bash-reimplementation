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
        return str(self.__class__) + ": " + str(self.__dict__)
        #return self.name

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


def cd(name, user, parent_folder):
    if name == '.':
        return parent_folder
    elif name == '..':
        if parent_folder.parent == None:
            print("cd: No such file or directory")
            return parent_folder
        return parent_folder.parent
    name += '/'
    for folder in parent_folder.get_items():
        if folder.get_name() == name:
            if type(folder) == Folder:
                return folder
            else:
                print("cd: Destination is a file")
                return parent_folder
    print("cd: No such file or directory")
    return parent_folder

def cd_dashp(name, user, parent_folder):
    pass

def ls(folder):
    for item in folder.get_items():
        print(item)

def mkdir(cmds, user, parent_folder):
    new_folder = Folder(cmds[1], user, parent_folder)
    #new_folder.add_parent_directory()
    new_folder.add_parent(parent_folder)
    return parent_folder.add_item(new_folder, user)

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
