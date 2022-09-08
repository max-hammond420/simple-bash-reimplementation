from objects import *
from execute import execute

def display_prompt(user, cwd):
    if cwd == '/':
        return f"{user}:{cwd}$ "
    return f"{user}:{cwd[:-1]}$ " 

def main():
    cmds = ['pwd', 'cd', 'mkdir', 'touch',
            'cp', 'mv', 'rm', 'rmdir',
            'chmod', 'chown', 'adduser', 'deluser', 'su', 'ls']

    users = ['root']
    current_user = users[0]
    root = Folder('', current_user)
    cwd = root

    while True:

        cmd = str(input(display_prompt(current_user, pwd(cwd, root))))

        full_cmd = cmd.split(' ')
        if full_cmd[0] in cmds:
            if full_cmd[0] == 'cd':
                if len(full_cmd) <= 1:
                    print("cd: Invalid syntax")
                    continue

                if full_cmd[1][0] == '/':
                    cwd = root
                    full_cmd[1] = full_cmd[1][1:]

                cwd = cd(full_cmd[1], current_user, cwd, root)

            execute(full_cmd, current_user, cwd, root)
        elif full_cmd[0] == "exit":
            break
        else:
            print(f"{full_cmd[0]}: command not found")
    print(f"bye, {current_user}")

if __name__ == '__main__':
    main()
