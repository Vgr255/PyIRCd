import events
import parse

class MissingDict(dict):
    def __missing__(self, name):
        result = Channel(name)
        self[name] = result
        return result

_channels = MissingDict()

exists = _channels.__contains__
get = _channels.__getitem__

class Channel:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.modes = {
            "no_parameter": [],
            "single_parameter": [],
        }

    def u_join(self, data):
        self.users.append(user)

    def u_part(self, data):
        self.users.remove(user)
        if not self.users:
            del _channels[self.name]

    def u_quit(self, data):
        pass

    def u_mode(self, user, target, modes):
        pass


