 
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
    username = "kar3k"
    
    delete_user(username)