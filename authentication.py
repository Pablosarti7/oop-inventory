class Authentication:

    def __init__(self, user) -> None:
        self.user = user
        self.user_status = {}
        self.current_user = None
    
    def login(self, email: str, password: str):
        user_database = self.user.user_db
        if email in user_database:
            if user_database[email]['Email'] == email and user_database[email]["Password"] == password:
                self.user_status[email] = True
                self.current_user = email
                return True
            else:
                return False
        else:
            return 'You are not registered'


    def logout(self, email):
        if email in self.user_status:
            self.user_status[email] = False
            self.current_user = None
        else:
            return 'User not found'

    def register(self, name: str, email: str, password: str):
        if email in self.user.user_db:
            return 'Email already exist'
        else:
            self.user.user_db[email] = {'Name': name, 'Email': email, 'Password': password}

