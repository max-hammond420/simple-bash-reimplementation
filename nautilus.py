from objects import File, Folder
from execute import execute
from commands import *


def display_prompt(user, cwd, root):
    if cwd == root:
        return f"{user}:{pwd(cwd, root)}$ "
    s = f"{user}:{pwd(cwd, root)}$ "
    return s


def main():
    cmds = ['pwd', 'cd', 'mkdir', 'touch',
            'cp', 'mv', 'rm', 'rmdir',
            'chmod', 'chown', 'adduser', 'deluser', 'su', 'ls']

    users = ['root']
    current_user = users[0]
    root = Folder('', current_user)

    cwd = root
    while True:

        cmd = str(input(display_prompt(current_user, cwd, root)))

        full_cmd = cmd.split(' ')
        if full_cmd[0] in cmds:

            if full_cmd[0] == 'cd':
                cwd = cd(full_cmd[1:], cwd, current_user, root)

            elif full_cmd[0] == 'adduser':
                if len(full_cmd) == 2:
                    if current_user == 'root':
                        users.append(full_cmd[1])
                    else:
                        print("adduser: Must be root")
                else:
                    print("adduser: Invalid syntax")

            elif full_cmd[0] == 'deluser':
                if len(full_cmd) == 2:
                    if current_user == 'root':
                        if full_cmd[1] in users:
                            users.remove(full_cmd[1])
                        else:
                            print("deluser: The user does not exist")
                    else:
                        print("deluser: Must be root")
                else:
                    print("deluser: Invalid syntax")

            elif full_cmd[0] == 'su':
                if len(full_cmd) == 2:
                    if full_cmd[1] in users:
                        current_user = full_cmd[1]
                    else:
                        print("su: Invalid user")
                elif len(full_cmd) == 1:
                    if 'root' in users:
                        current_user = 'root'
                    else:
                        print("su: Invalid user")
                else:
                    print("su: Invalid syntax")

            else:

                execute(full_cmd, current_user, cwd, root)
        elif full_cmd[0] == "exit":
            break
        else:
            print(f"{full_cmd[0]}: command not found")
    print(f"bye, {current_user}")


if __name__ == '__main__':
    main()
