from .user import User

class MHWP(User):
    def __init__(self, username, password,):
        super().__init__(username, password, role='MHWP')