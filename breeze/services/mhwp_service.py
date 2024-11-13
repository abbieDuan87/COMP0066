from breeze.utils.cli_utils import print_system_message, clear_screen, direct_to_dashboard
from breeze.utils.constants import MHWP_BANNER_STRING

class MHWPService:
    def __init__(self, auth_service):
        self.auth_service = auth_service
        

    def show_mhwp_dashboard(self, user):
        """
        Displays the MWHP dashboard and processes user actions.

        Args:
            user (User): _The logged-in user
            
        Returns:
            bool: True if the user chose to log out, otherwise False
        """
    
        clear_screen()
        print(MHWP_BANNER_STRING)
        print('Hi', user.get_username(), '!')
        print('What do you want to do today?')

        while True:
                print("[C] View Calendar of Appointments")
                print("[M] Manage Appointments (Confirm or Cancel)")
                print("[A] Add Patient Information (Condition, Notes)")
                print("[D] Display Patient Summary with Mood Chart")
                print("[X] Log out")

                user_input = input("> ").strip().lower()
                match user_input:
                    case "c":
                        self.view_calendar(user)
                    case "m":
                        self.manage_appointments(user)
                    case "a":
                        self.add_patient_information(user)
                    case "d":
                        self.display_patient_summary(user)
                    case "x":
                        return True 
                    case _:
                        print_system_message("Invalid choice. Please try again.")

    def view_calendar(self, user):
        print_system_message('Feature to view calendar to be implemented soon')

    def manage_appointments(self, user):
        print_system_message('Feature to manage appointments to be implemented soon')

    def add_patient_information(self, user):
        print_system_message('Feature to add paient info to be implemented soon')

    def display_patient_summary(self, user):
        print_system_message('Feature to display patient summary to be implemented soon')