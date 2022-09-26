from objects import File, Folder
from commands import *


def execute(cmd: list, user, cwd, root) -> None:
    a = cmd[0]
    args = []
    if len(cmd) > 1:
        args = cmd[1:]

    # Part 1
    if a == "pwd":
        print(pwd(args, cwd, root))
    elif a == "mkdir":
        mkdir(args, cwd, user, root)
    elif a == "touch":
        touch(args, cwd, user, root)

    # Implement 2nd
    elif a == "cp":
        cp(args, cwd, root, user)
    elif a == "mv":
        mv(args, cwd, root, user)
    elif a == "rm":
        rm(args, cwd, root, user)
    elif a == "rmdir":
        rmdir(args, cwd, root, user)

    # TODO implement 3rd
    elif a == "chmod":
        chmod(args, cwd, root, user)
    elif a == "chown":
        pass
    elif a == "ls":
        print(ls(args, cwd, user, root), end='')
