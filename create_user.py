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
    username = "kar3k"
    password = "Psw0rd_kar3k"
    
    create_user(username, password)