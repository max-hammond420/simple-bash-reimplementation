class File():
    # group owner, permissions
    def __init__(self, name, owner, parent):
        # super().__init__(self, name, user)

        self.name = name
        self.owner = owner
        self.parent = parent

        # Read, Write, Execute
        self.owner_permissions = [True, True, False]
        self.other_permissions = [True, False, False]

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name == other.name

    def get_name(self):
        return self.name

    def get_parent(self):
        return self.parent

    def get_owner(self):
        return self.owner

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

        self.name = name
        self.owner = owner

        # Read, Write, Execute
        self.owner_permissions = [True, True, True]
        self.other_permissions = [True, False, True]

    def __str__(self):
        # return str(self.__class__) + ": " + str(self.__dict__)
        return self.name

    def get_parent(self):
        return self.parent

    def get_name(self) -> str:
        return self.name

    def get_items(self) -> list:
        return self.items

    def get_item_names(self) -> list:
        ls = []
        for i in range(len(self.items)):
            ls.append(self.items[i].get_name())
        return ls

    def get_child(self, name):
        # name: str
        for i in range(len(self.items)):
            if self.items[i].get_name() == name:
                return self.items[i]
        return None

    def get_owner(self):
        return self.owner

    def get_owner_permissions(self):
        return self.owner_permissions

    def get_other_permissions(self):
        return self.other_permissions

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
        ls = []
        for i in range(len(self.items)):
            ls.append(self.items[i].get_name())
        if name.get_name() in ls:
            return False

        self.items.append(name)

    def remove_item(self, name, user):
        for i in range(len(self.items)):
            if self.items[i].get_name() == name:
                self.items.pop(i)
                break

    def add_parent(self, parent):
        self.parent = parent

    def chmod(self, modify_string, place):
        pass
