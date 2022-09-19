from ctypes import wstring_at
from objects import File, Folder


def get_absolute_path(directory, cwd, root):
    # TODO: check functionality
    # directory: str e.g. /a/b/c or a/b/c
    # returns: [destination: list of child directories of root]
    # doesn't care if folder isnt syntactically correct
    directory = directory.split('/')
    if directory[0] == '':
        return directory[1:]

    destination = []
    ls = [cwd]

    # get cwd in a list, append directory
    while cwd.get_parent() is not None:
        ls.append(cwd.get_parent())
        cwd = cwd.get_parent()

    for i in range(len(ls)-1, -1, -1):
        destination.append(ls[i].get_name())
    destination.pop(0)

    return destination + directory


def conv_path_to_obj(path, root):
    # path is ['a', 'b', 'c']
    # iterates through an absolute path,
    # returns [list of child Folder objects] if path is correct
    # else returns False

    # intended to leave out the last file path from user input, depending on
    # the use of the parent function
    file_path = path

    if file_path == ['']:
        return [root]

    path_objects = [root]
    cwd = root

    for i in range(len(file_path)):
        if type(cwd) is File:
            return None
        cwd_item_names = cwd.get_item_names()
        if file_path[i] == '.':
            cwd = cwd
            path_objects.append(cwd)
        elif file_path[i] == '..':
            if cwd == root:
                path_objects.append(cwd)
            else:
                cwd = cwd.get_parent()
                path_objects.append(cwd)
        elif file_path[i] in cwd_item_names:
            cwd = cwd.get_child(file_path[i])
            path_objects.append(cwd)
        else:
            return None

    return path_objects


def check_valid_path(path):
    # takes in file a list of file objects and returns true if it is a
    # valid path_check
    if path is None:
        return False
    for i in range(len(path)-1):
        if type(path[i]) is not Folder or type(path[i+1]) is not Folder:
            return False
        if path[i+1].get_name() not in path[i].get_item_names():
            return False
    return True


def pwd(cwd, root):
    ls = [cwd.get_name()]

    # get cwd in a list, append directory
    while cwd.get_parent() is not None:
        ls.append(cwd.get_parent().get_name())
        cwd = cwd.get_parent()

    path = ''
    for i in range(len(ls)):
        path += ls[len(ls)-1-i] + '/'

    if len(path) > 1:
        path = path[:-1]
    return path


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
    if len(args) != 1 or len(args) == 0:
        print("cd: Invalid syntax")
        return cwd

    path = args[0]
    path = get_absolute_path(path, cwd, root)
    path_obj = conv_path_to_obj(path, root)
    if path_obj is None:
        print("cd: No such file or directory")
        return cwd

    if type(path_obj[-1]) is not Folder:
        print("cd: Destination is a file")
        return cwd

    path = check_valid_path(path_obj)

    return path_obj[-1]


def mkdir(args, cwd, user, root):
    # iterate through path[:-2]
    # if path[i+1] is not a child of path[i], return error msg
    # if add path[-1] to path[-2].items
    dash_p = False
    if '-p' in args:
        dash_p = True
        args.remove('-p')

    if len(args) != 1:
        print("mkdir: Invalid syntax")
        return None

    path = args[0]
    new_folder_name = args[0][-1]

    path = get_absolute_path(path, cwd, root)
    new_folder_name = path[-1]
    path = path[:-1]

    path = conv_path_to_obj(path, root)
    if check_valid_path(path) is False:
        print("mkdir: Ancestor directory does not exist")
        return None

    new_folder = Folder(new_folder_name, user, path[-1])
    new_folder.add_parent(path[-1])
    parent = path[-1].add_item(new_folder, user)
    if parent is False:
        print("mkdir: File exists")
        return None


def touch(args, cwd, user, root):
    # iterate through path[:-2]
    # if path[i+1] is not a child of path[i], return error msg
    # if add path[-1] to path[-2].items

    if len(args) != 1:
        print("touch: Invalid syntax")
        return None

    path = args[0]
    new_folder_name = args[0][-1]

    path = get_absolute_path(path, cwd, root)
    new_folder_name = path[-1]
    path = path[:-1]

    path = conv_path_to_obj(path, root)
    if not check_valid_path(path):
        print("touch: Ancestor directory does not exist")
        return None

    new_folder = File(new_folder_name, user, path[-1])
    parent = path[-1].add_item(new_folder, user)
    if parent is False:
        print("touch: File exists")
        return None


def cp(args, cwd, root, user):
    if len(args) != 2:
        print("cp: Invalid syntax")
        return None

    src = get_absolute_path(args[0], cwd, root)
    dst = get_absolute_path(args[1], cwd, root)

    src_file_name = src[-1]
    src = src[:-1]
    dst_file_name = dst[-1]
    dst = dst[:-1]

    src = conv_path_to_obj(src, root)
    dst = conv_path_to_obj(dst, root)

    if type(dst[-1].get_child(dst_file_name)) is Folder:
        print("cp: Destination is a directory")
        return None

    if dst[-1].get_child(dst_file_name) is not None:
        print("cp: File exists")
        return None

    if type(src[-1].get_child(src_file_name)) is Folder:
        print("cp: Source is a directory")
        return None

    if check_valid_path(src) is False:
        print("cp: No such file")
        return None

    if check_valid_path(dst) is False:
        print("cp: No such file or directory")
        return None

    if src[-1].get_child(src_file_name) is None:
        print("cp: No such file")
        return None

    new_file = File(dst_file_name, user, dst[-1])
    parent = dst[-1].add_item(new_file, user)


def mv():
    pass


def rm():
    pass


def rmdir():
    pass
