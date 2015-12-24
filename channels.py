import events
import parse

class ChannelDict(dict):
    def __missing__(self, name):
        result = Channel(name)
        self[name] = result
        return result

_channels = ChannelDict()

exists = _channels.__contains__
get = _channels.__getitem__

class Channel:
    def __init__(self, name):
        self.name = name
        self.users = {}
        self.invite_only = False
        self.key = None
        self.throttle = None
        self.limit = None
        self.forward = None
        self.ops = set()
        self.voices = set()
        self.bans = set()
        self.quiets = set()
        self.exempts = set()
        self.invites = set()
        self.modes = set()

    def join(self, user, key):
        self.users[user.name] = user

    def u_part(self, data):
        self.users.remove(user)
        if not self.users:
            del _channels[self.name]

    def u_quit(self, data):
        pass

    def u_mode(self, user, target, modes):
        pass


