_users = []

exists = users.__contains__

def get(nick, ident, host, real):
    for user in users:
        if user.ident == ident:
            return user

    result = User(nick, ident, host, real)
    users.append(result)
    return result

class User:
    def __init__(self, nick, ident, host, real):
        self.nick = nick
        self.ident = ident
        self.host = host
        self.real = real
         
        self.channels = []

    def __str__(self):
        return "{self.nick}!{self.ident}@{self.host}".format(self=self)
