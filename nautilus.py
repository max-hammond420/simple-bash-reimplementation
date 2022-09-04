import commands.commands1 as commands1
import commands.commands2 as commands2
import commands.commands3 as commands3

def execute(cmd: list) -> None:
    a = cmd[0]
    ### TODO Implement first
    if a == "exit":
        exit_file.exit_cmd('$')
    elif a == "pwd":
        pass
    elif a == "cd":
        pass
    elif a == "mkdir":
        pass
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

def display_prompt(user: str, path: str) -> str:
    pass

def main():
    cmds = ['exit', 'pwd', 'cd', 'mkdir', 'touch',
            'cp', 'mv', 'rm', 'rmdir',
            'chmod', 'chown', 'adduser', 'deluser', 'su', 'ls']

    while True:
        #cmd = str(input(display_prompt()))
        cmd = str(input("$ "))
        full_cmd = cmd.split(' ')
        if full_cmd[0] in cmds:
            execute(full_cmd)



if __name__ == '__main__':
    main()
