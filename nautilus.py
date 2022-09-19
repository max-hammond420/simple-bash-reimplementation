from objects import File, Folder
from execute import execute
from commands import *


def display_prompt(user, cwd, root):
    if cwd == root:
        return f"{user}:{pwd(cwd, root)}$ "
    s = f"{user}:{pwd(cwd, root)}$ "
    return s


def adduser(users, current_user, full_cmd):
    if len(full_cmd) != 1:
        print("adduser: Invalid Syntax")
        return users

    if current_user != 'root':
        print("Must be root")
        return users

    else:
        return users.append(full_cmd[0])


def deluser(users, current_user, full_cmd):
    if len(full_cmd) != 1:
        print("deluser: Invalid Syntax")
        return users

    if current_user != 'root':
        print("Must be root")
        return users

    else:
        if full_cmd[0] in users:
            return users.remove(full_cmd[0])
        else:
            print("deluser: The user does not exist")
            return users


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
                users = adduser(current_user, users, full_cmd[1:])

            elif full_cmd[0] == 'deluser':
                users = deluser(current_user, users, full_cmd[1:])

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
