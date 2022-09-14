from ctypes import wstring_at
from objects import File, Folder


def get_absolute_path(directory, cwd, root):
    # TODO: check functionality
    # directory: str e.g. /a/b/c or a/b/c
    # returns: [cwd: Folder, destination: list of child directories of root]
    # doesn't care if folder isnt syntactically correct
    directory = directory.split('/')
    if directory[0] == '':
        return [root, directory[1:]]

    destination = []
    ls = [cwd]

    # get cwd in a list, append directory
    while cwd.get_parent() is not None:
        ls.append(cwd.get_parent())
        cwd = cwd.get_parent()

    for i in range(len(ls)-1, -1, -1):
        destination.append(ls[i].get_name())

    return [root, destination]


def conv_path_to_obj(path):
    # path is [root, [path]]
    # iterates through an absolute path,
    # returns [list of child Folder objects] if path is correct
    # else returns False

    # intended to leave out the last file path from user input, depending on
    # the use of the parent function
    print('36', path)
    root = path[0]
    file_path = path[1]

    path_objects = [root]
    cwd = root

    for i in range(len(file_path)):
        cwd_item_names = cwd.get_item_names()
        if file_path[i] in cwd_item_names:
            cwd = cwd.get_child(file_path[i])
            path_objects.append(cwd)
        else:
            return None

    return path_objects


def check_valid_path(path):
    # takes in file a list of file objects and returns true if it is a
    # valid path_check
    for i in range(len(path)-1):
        if type(path[i]) is not Folder or type(path[i+1]) is not Folder:
            return False
        if path[i+1].get_name() not in path[i].get_item_names():
            return False
    return True


def pwd(current_directory):
    ls = [current_directory]
    while current_directory.get_parent() is not None:
        ls.append(current_directory.get_parent())
        current_directory = current_directory.get_parent()

    s = ''
    for i in range(len(ls)-1, -1, -1):
        s += ls[i].get_name()+'/'
    return s


def ls(current_directory):
    s = ''
    for item in current_directory.get_items():
        if type(item) == Folder:
            s += (item.get_name() + ' ')
        else:
            s += (item.get_name() + ' ')

    return s


def cd(args, cwd, user, root):
    # iterate through path
    # check that cwd.get_child(path[i]) is not None, else, error
    # return path[-2].get_child(path[-1])
    if len(args) != 1:
        print('cd: Invalid syntax')

    path = args[0]
    path = parse_destination(path, cwd, root)
    print('path', path)

    path_check = check_path(path[:-1], root)
    if type(path_check) == bool:
        print("cd: No such file or directory")
        return cwd

    for i in range(len(path)):
        if path[i] == '..':
            cwd = cwd.get_parent()
        elif path[i] == '.':
            cwd = cwd
        else:
            cwd = path[i]

    return cwd


def mkdir(args, cwd, user, root):
    # iterate through path[:-2]
    # if path[i+1] is not a child of path[i], return error msg
    # if add path[-1] to path[-2].items
    dash_p = False
    if '-p' in args:
        dash_p = True
        args.remove('-p')

    if len(args) != 1:
        print("mkdir: invalid syntax")

    path = args[0][:-1]
    new_folder_name = args[0][-1]

    path = get_absolute_path(path, cwd, root)
    path = conv_path_to_obj(path)
    if path is None:
        print("mkdir: Ancestor directory does not exist")
        return None
    path = check_valid_path(conv_path_to_obj(path))
    print('136', path)

    new_folder = Folder(new_folder_name, user, path[-1])
