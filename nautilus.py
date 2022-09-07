from objects import *
import commands.execute as execute

def display_prompt(user: str, path: str) -> str:
    pass

def main():
    cmds = ['pwd', 'cd', 'mkdir', 'touch',
            'cp', 'mv', 'rm', 'rmdir',
            'chmod', 'chown', 'adduser', 'deluser', 'su', 'ls']

    users = ['root']
    root = Folder('/', users[i])

    while True:

        ### REPLACE WITH DISPLAY_PROMPT()
        #cmd = str(input(display_prompt()))
        cmd = str(input("$ "))

        full_cmd = cmd.split(' ')
        if full_cmd[0] in cmds:
            execute.execute(full_cmd)
        elif full_cmd[0] == "exit":
            break
    print("Bye, <current user>")

if __name__ == '__main__':
    main()
