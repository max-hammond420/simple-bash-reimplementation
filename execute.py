from objects import File, Folder
from commands import *


def execute(cmd: list, user, cwd, root) -> None:
    a = cmd[0]
    args = []
    if len(cmd) > 1:
        args = cmd[1:]
    # print(args)
    # Part 1
    if a == "pwd":
        if pwd(cwd) == pwd(root):
            print(pwd(cwd))
        else:
            print(pwd(cwd)[:-1])
    elif a == "mkdir":
        mkdir(args, cwd, user, root)
    elif a == "touch":
        touch(cwd, cmd[1], user)

    # TODO Implement 2nd
    elif a == "cp":
        cp(cmd[1], cmd[2], user, cwd, root)
    elif a == "mv":
        mv(cmd[1], cmd[2], user, cwd, root)
    elif a == "rm":
        pass
    elif a == "rmdir":
        pass

    # TODO implement 3rd
    elif a == "chmod":
        pass
    elif a == "chown":
        pass
    elif a == "adduser":
        pass
    elif a == "deluser":
        pass
    elif a == "su":
        pass
    elif a == "ls":
        print(ls(cwd))
