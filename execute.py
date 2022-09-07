from exe_mkdir import mkdir as mkdir

def execute(cmd: list) -> None:
    a = cmd[0]
    ### TODO Implement first
    if a == "pwd":
        pass
    elif a == "cd":
        pass
    elif a == "mkdir":
        mkdir()
    elif a == "touch":
        pass

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
        pass

