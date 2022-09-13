from objects import File, Folder


def get_every_folder(s):
    # takes in string /a/b/c -> ['', 'a', 'b', 'c']
    # or a/b/c -> ['a', 'b', 'c']
    s = s.split('/')
    return s


def parse_directory(directory, cwd, root):
    # cwd: Folder object
    # directory: list of names: str
    directory = get_every_folder(directory)
    if directory[0] == '':
        cwd = root
        directory = directory[1:]

    return [cwd, directory]


def parse_destination(parsed_directory):
    # parsed_dorectory is [cwd, directory: list of strings]
    # returns: [directory[-2], directory[-1]]
    # errors if each proceeding directory is not in it's parent directory
    cwd = parsed_directory[0]
    directory_ls = parsed_directory[1]

    for i in range(len(directory_ls[:-1])):
        if cwd.get_child(directory_ls[i]).get_name() == directory_ls[i]+'/':
            cwd = cwd.get_child(directory_ls[i])
        else:
            return None

    child = cwd.get_child(directory_ls[-1]).get.name()

    if child == directory_ls[-1] or child == directory_ls[-1] + '/':
        return [cwd, cwd.get_child(directory_ls[-1])]
    return None


def cd(name, user, parent_folder, root):
    if name == '.':
        return parent_folder
    elif name == '..':
        if parent_folder.parent is None:
            return root
        return parent_folder.parent
    if name == '':
        return root
    name += '/'
    for folder in parent_folder.get_items():
        if type(folder) == File and folder.get_name() == name[:-1]:
            print("cd: Destination is a file")
            return parent_folder

        if folder.get_name() == name:
            if type(folder) == Folder:
                return folder

    print("cd: No such file or directory")
    return parent_folder


"""
def ls(folder):
    for item in folder.get_items():
        print(item)
"""


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
    # print(new_folder_name, parent_folders)
    new_folder = Folder(new_folder_name, user, cwd)
    # print(parent_folders[-1])
    # print(cwd)
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
    # TODO implement paths
    new_file = File(name, user)
    parent_folder.add_item(new_file, user)


def pwd(current_directory):
    ls = [current_directory]
    while current_directory.get_parent() is not None:
        ls.append(current_directory.get_parent())
        current_directory = current_directory.get_parent()

    s = ''
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


def cp(src, dst, user, cwd, root):
    src = parse_directory(src, cwd, root)
    dst = parse_directory(dst, cwd, root)
    # check if src is a file
    # src_cwd is a Folder object
    src_cwd = src[0]

    # src_path is a list of strings
    src_path = src[1]
    for i in range(len(src_path[:-1])):
        src_cwd_item_names = []
        for j in range(len(src_cwd.items)):
            src_cwd_item_names.append(src_cwd.items[i].get_name())

        if src_path[i]+'/' in src_cwd_item_names:
            # print('src_cwd', type(src_cwd))
            # print('src_path[i],', type(src_path[i]))
            print('src_cwd.items', src_cwd.items)
            # print('get_child i', type(src_cwd.get_child(src_path[i])))
            if type(src_cwd.get_child(src_path[i]+'/')) == Folder:
                src_cwd = src_cwd.get_child(src_path[i]+'/')
                print('src_cwd', src_cwd)
            else:
                print("cp: Source is a file")
                return None
        else:
            print("cp: Source doesnt exist")
            return None

    if src_cwd.get_child(src_path[-1]).get_name() == src_path[-1]:
        cp_file = src_cwd.get_child(src_path[-1])
        print(type(cp_file))
        if type(cp_file) != File:
            print("cp: Source is a file")
            return None
    else:
        print("cp: Source doesn't exist")
        return None

    # dst
    dst_path = dst[1]
    for i in range(len(dst_path)):
        src_cwd_item_names = []
        for j in range(len(src_cwd.items)):
            src_cwd_item_names.append(src_cwd.items[i].get_name())

        if src_path[i]+'/' in src_cwd_item_names:
            # print('src_cwd', type(src_cwd))
            # print('src_path[i],', type(src_path[i]))
            print('src_cwd.items', src_cwd.items)
            # print('get_child i', type(src_cwd.get_child(src_path[i])))
            if type(src_cwd.get_child(src_path[i]+'/')) == Folder:
                src_cwd = src_cwd.get_child(src_path[i]+'/')
                print('src_cwd', src_cwd)
            else:
                print("cp: Source is a file")
                return None
        else:
            print("cp: Source doesnt exist")
            return None

    # dst_cwd.add_item(cp_file)


def mv(src, dst, user):
    pass


def rm(path, dst, user):
    pass


def rmdir(directory, user):
    pass


def chmod():
    pass
