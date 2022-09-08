from objects import *

def execute(cmd: list, user, cwd) -> None:
    a = cmd[0]
    ### TODO Implement first
    if a == "pwd":
        print(pwd(cwd))
    elif a == "mkdir":
        mkdir(cmd, user, cwd)
    elif a == "touch":
        touch(cwd, cmd[1], user)


    ### TODO Implement 2nd
    elif a == "cp":
        pass
    elif a == "mv":
        pass
    elif a == "rm":
        pass
    elif a == "rmdir":
        pass

    ### TODO implement 3rd
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

