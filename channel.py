def _check(s):
    if not isinstance(s, Channel):
        raise TypeError("first argument to Channel method "
                        "must be a Channel object")

_channels = []

exists = _channels.__contains__

def get(name):
    assert isinstance(name, str), "channel name must be a string"
    for chan in _channels:
        assert isinstance(chan, Channel), "stored channel must be a Channel"
        if chan.name == name:
            return chan

    result = Channel(name)
    _channels.append(result)
    return result

class Channel:
    def __init__(self, name):
        _check(self)
        self.name = name
        self.users = []
        self.modes = {
            "no_parameter": [],
            "single_parameter": [],
        }

    def u_join(self, user):
        _check(self)
        self.users.append(user)

    def u_part(self, user):
        _check(self)
        self.users.remove(user)
        if not self.users:
            _channels.remove(self)

    u_quit = u_part

    def u_mode(self, user, target, modes):
        _check(self)


