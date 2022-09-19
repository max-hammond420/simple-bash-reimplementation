from objects import File, Folder
from commands import *


def execute(cmd: list, user, cwd, root) -> None:
    a = cmd[0]
    args = []
    if len(cmd) > 1:
        args = cmd[1:]

    # Part 1
    if a == "pwd":
        print(pwd(cwd, root))
    elif a == "mkdir":
        mkdir(args, cwd, user, root)
    elif a == "touch":
        touch(args, cwd, user, root)

    # TODO Implement 2nd
    elif a == "cp":
        cp(args, cwd, root, user)
    elif a == "mv":
        mv(args, cwd, root, user)
    elif a == "rm":
        mv(args, cwd, root, user)
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
