1. To download files in linux use below bash command.
```shell
    $ sudo git clone https://github.com/vr-kar3k/create-user.git
```
2. After successfully downloaded, go to the folder 
```shell
   $ cd create-user
```
3. execute bash command 

to create 
```shell
    $ sudo python3 create_user.py
```
to delete
```shell
    $ sudo python3 delete_user.py
```

Note: if u want to delete folder completely use this bash command

```shell
    $ sudo rm -rf create-user
```
-----------------------------------------------------------------------------------------------------


if you need detailed information look below 

To create a user and set a password automatically in Ubuntu using a Python script along with bash commands, you can combine subprocess calls to execute the necessary commands. Here’s an example Python script that accomplishes this:

1. Python file (create_user.py):

This script will create a new user and set a password using bash commands.

```shell
import subprocess

def create_user(username, password):
    try:
        # Create the user with no password (bash command: sudo useradd)
        subprocess.run(['sudo', 'useradd', '-m', username], check=True)
        
        # Set the password for the user (bash command: echo "username:password" | sudo chpasswd)
        subprocess.run(['sudo', 'bash', '-c', f'echo "{username}:{password}" | sudo chpasswd'], check=True)

        print(f"User {username} created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error creating user {username}: {e}")

if __name__ == "__main__":
    # Define the username and password
    username = "your username"  # Replace with your desired username
    password = "your password"  # Replace with your desired password
    
    create_user(username, password)
```
How this script works:

1. subprocess.run(): Runs a shell command from within Python. In this case, it creates a user using useradd and sets the password using chpasswd.

2. -m flag: Ensures that the user's home directory is created.

3. chpasswd: Sets the password for the user.



How to run:

1. Save the Python script (create_user.py).

2. Give it execution permission:
```shell
chmod +x create_user.py
```

3. Run the script using sudo:
```shell
sudo python3 create_user.py
```

This will create the user and set the password as specified in the script.

______________________________________________________________________________________________


To delete a user and their home directory in Ubuntu using a Python script with bash commands, you can use the userdel command. Here’s the modified Python script to delete the user:
```shell
import subprocess

def delete_user(username):
    try:
        # Delete the user and remove their home directory (bash command: sudo userdel -r username)
        subprocess.run(['sudo', 'userdel', '-r', username], check=True)

        print(f"User {username} deleted successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting user {username}: {e}")

if __name__ == "__main__":
    # Define the username
    username = "your username"
    
    delete_user(username)
```
How this script works:

subprocess.run(): Executes the userdel command with the -r flag, which removes the user's home directory as well.

-r flag: Ensures that the user's home directory and mail spool are deleted along with the account.


Steps to execute:

1. Save the script as delete_user.py.

2. Make it executable:
```shell
    $ chmod +x delete_user.py
```
3. Run the script with sudo:

```shell
    $ sudo python3 delete_user.py
```
This will delete the user and their home directory.
