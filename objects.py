class Item:
    def __init__(self, name):
        self.name = name

    # create an add child method
    def add_child(self, name):
        pass

class File():
    # group owner, permissions
    def __init__(self, name, owner):
        #super().__init__(self, name, user)

        self.name = name
        self.owner = owner

        # Read, Write, Execute
        self.owner_permissions = [True, True, False]
        self.other_permissions = [True, False, False]

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
    def __init__(self, name: str, owner: str):

        #super().__init__(self, name)

        self.items = []

        self.name = name
        self.owner = owner

        # Read, Write, Execute
        self.owner_permissions = [True, True, True]
        self.other_permissions = [True, False, True]

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def add_parent_directory(self) -> None:
        # only use if folder is not root
        self.items.append('.')
        self.items.append('..')

    def get_name(self) -> str:
        return self.name

    def get_items(self) -> list:
        for i in range(len(self.items)):
            print(self.items[i])
        return self.items

    def add_folder(self, name):
        # add children
        self.items.append(name)

    def touch(self, name, location='.'):
        self.items.append(File(name))

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

    def mkdir(self):
        pass

    def touch(self):
        pass
