# Status: Conceptual

class UserDict(dict):
    def __missing__(self, name):
        result = User(*name)
        self[name[0]] = result
        return result

_users = UserDict()

def exists(nick, ident, host, real):
    return (nick, ident, host, real) in _users

def get(nick, ident, host, real):
    return _users[nick, ident, host, real]

class User:

    def __init__(self, nick, ident, host, real):
        self._nick = nick
        self._ident = ident
        self._host = host
        self._real = real
         
        self.channels = set()

    def __str__(self):
        return "{self.nick}!{self.ident}@{self.host}".format(self=self)
