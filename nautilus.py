from objects import File, Folder
from execute import execute
from commands import *


def display_prompt(user, cwd, root):
    args = []
    if cwd == root:
        return f"{user}:{pwd(args, cwd, root)}$ "
    s = f"{user}:{pwd(args, cwd, root)}$ "
    return s


def main():

    # Setting initial variables

    # Every single command to implement
    cmds = ['pwd', 'cd', 'mkdir', 'touch',
            'cp', 'mv', 'rm', 'rmdir',
            'chmod', 'chown', 'adduser', 'deluser', 'su', 'ls']

    # Initial user is only root
    users = ['root']
    # Setting the user to be root when begining program
    current_user = users[0]

    # Creating root directory and making the cwd root
    root = Folder('', current_user)
    cwd = root

    # Main loop of the program, doesnt quit until exit has been given
    while True:

        cmd = str(input(display_prompt(current_user, cwd, root)))

        cmd = cmd.strip()

        if cmd == "":
            continue

        full_cmd = cmd.split(' ')
        if full_cmd[0] in cmds:

            # Handling the current directory as a variable in main function
            if full_cmd[0] == 'cd':
                cwd = cd(full_cmd[1:], cwd, current_user, root)

            # Also handling adduser, deluser and su in the main function
            elif full_cmd[0] == 'adduser':
                if len(full_cmd) == 2:
                    if current_user == 'root':
                        if full_cmd[1] in users:
                            print("adduser: The user already exists")
                        else:
                            users.append(full_cmd[1])
                    # Error handling below
                    else:
                        print("adduser: Operation not permitted")
                else:
                    print("adduser: Invalid syntax")

            # Deluser handling
            elif full_cmd[0] == 'deluser':
                if len(full_cmd) == 2:
                    if current_user == 'root':
                        if full_cmd[1] in users:
                            if full_cmd[1] == 'root':
                                # Warning msg
                                print("WARNING: You are just about to delete the root account")
                                print("Usually this is never required as it may render the whole system unusable")
                                print("If you really want this, call deluser with parameter --force")
                                print("(but this `deluser` does not allow `--force`, haha)")
                                print("Stopping now without having performed any action")
                            else:
                                users.remove(full_cmd[1])
                        # Error handling below
                        else:
                            print("deluser: The user does not exist")
                    else:
                        print("deluser: Operation not permitted")
                else:
                    print("deluser: Invalid syntax")

            # Su command
            elif full_cmd[0] == 'su':
                if len(full_cmd) == 2:
                    if full_cmd[1] in users:
                        current_user = full_cmd[1]
                    else:
                        print("su: Invalid user")
                # Switching the current user
                elif len(full_cmd) == 1:
                    if 'root' in users:
                        current_user = 'root'

                    # Error handling
                    else:
                        print("su: Invalid user")
                else:
                    print("su: Invalid syntax")

            else:

                execute(full_cmd, current_user, cwd, root)
        elif full_cmd[0] == "exit":
            if len(full_cmd) != 1:
                print("exit: Invalid syntax")
            else:
                break
        else:
            print(f"{full_cmd[0]}: Command not found")
    print(f"bye, {current_user}")


if __name__ == '__main__':
    main()
