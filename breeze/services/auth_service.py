from breeze.models.admin import Admin
from breeze.models.patient import Patient
from breeze.models.mhwp import MHWP

from breeze.utils.cli_utils import print_system_message, direct_to_dashboard
from breeze.utils.data_utils import load_data, save_data

class AuthService:
    def __init__(self):
        self.users = {user.get_username(): user for user in load_data("./data/users.json").get("users", [])}
        self.current_user = None
    
    def save_data_to_file(self):
        """Save the updated user data to the JSON file"""
        data = {"users": [user.to_dict() for user in self.users.values()]}
        save_data("./data/users.json", data)

    def login(self):
        while True:
            username = input("Username: ").strip()
            if not username:
                print_system_message("Username cannot be empty. Please try again.")
                continue
            break
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
        while True:
            username = input("Username: ").strip()
            if not username:
                print_system_message("Username cannot be empty. Please try again.")
                continue
            if username in self.users:
                print_system_message("Username already taken! Please choose another.")
                continue
            break

        password = input("Password: ")
        
        # Display role options
        print("Please choose a role:\n[A]dmin\n[P]atient\n[M]HWP")
        
        while True:
            role = input("Select a role [A/P/M]: ").strip().lower()
            # Register role based on input
            new_user = self._register_role(role, username, password)
            if new_user:
                break  
        
        # save the new user into the self.users dictionary
        self.users[new_user.get_username()] = new_user
        self.save_data_to_file()
        direct_to_dashboard("Account created successfully!")

    def get_all_users(self):
        return self.users