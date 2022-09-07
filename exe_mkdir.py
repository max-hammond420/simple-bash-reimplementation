from objects import *

def mkdir(parent_folder, args, user) -> None:

    # parent 

    # TODO check permissions
    #if not(check_perms):
        #print

    # TODO if -p flag, recursively use on each / /
    #if args[1] == '-p':
    #   if args[2] == 

    name = args[1]
    parent_folder.add_folder(name, user).add_parent_directory()
