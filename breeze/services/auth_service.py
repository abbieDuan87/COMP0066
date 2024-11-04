from breeze.models.admin import Admin
from breeze.models.patient import Patient
from breeze.models.mhwp import MHWP

from breeze.utils.cli_utils import print_system_message

class AuthService:
    def __init__(self):

        self.users = {
            "admin": Admin("admin", "1234567"),
            "patient1": Patient("patient1", "1234567"),
            "mhwp1": MHWP("mhwp1", "1234567")
        }
        
        self.current_user = None

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        user = self.users.get(username)
        if user and user.login(password):
            print(f"Welcome, {username}")
            self.current_user = user
            return user
        return None
    
    def logout(self):
        if self.current_user:
            self.current_user = None
            return None
    
    def _register_role(self, role, username, password):   
        """Helper method to create a new user based on role.
        Args:
            role (str)
            username (str)
            password (str)
        """  
        match role.strip().lower():
            case "a":
                return Admin(username, password)
            case "p":
                return Patient(username, password)
            case "m":
                return MHWP(username, password)
            case _:
                print_system_message("Invalid role! Please select a valid option.")
                return None

    def register(self):
        """A function to register new user

        Returns:
            user (Admin/Patient/MHWP): The created new user
        """
        username = input("Username: ")
        
        # Check if username already exists
        if username in self.users:
            print_system_message("Username already taken! Please choose another.")
            return None

        password = input("Password: ")
        
        # Display role options
        print("Please choose a role:\n[A]dmin\n[P]atient\n[M]HWP")
        
        while True:
            role = input("Select a role [A/P/M]: ").strip().lower()
            # Register role based on input
            new_user = self._register_role(role, username, password)
            if new_user:
              break  
        
        self.users[username] = new_user
        print_system_message("Account created successfully! Press B to go back and log in.")
        return new_user