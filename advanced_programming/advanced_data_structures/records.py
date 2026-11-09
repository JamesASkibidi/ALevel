# record User:
#   userID : string
#   first_name : string
#   last_name : string
#   active : boolean
#   balance : real


users = []

class User:
    def __init__(self, first_name, last_name, active=False, balance=0):
        self.userID = len(users) + 1
        self.first_name = first_name
        self.last_name = last_name
        self.active = active
        self.balance = balance

def activate_account(user):
    user.active = True


new_user = User('rafferty' , 'shanoon')

users.append(new_user)

activate_account(new_user)

print(users[0].active)