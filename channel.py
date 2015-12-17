def _check(s):
    if not isinstance(s, Channel):
        raise TypeError("first argument to Channel method "
                        "must be a Channel object")

channels = []

def get_channel(name):
    assert isinstance(name, str), "channel name must be a string"
    for chan in channels:
        assert isinstance(chan, Channel), "stored channel must be a Channel"
        if chan.name == name:
            return chan

    result = Channel(name)
    channels.append(result)
    return result

class Channel:
    def __init__(self, name):
        _check(self)
        self.name = name
        self.users = []

    def u_join(self, user):
        _check(self)
        self.users.append(user)

    def u_part(self, user):
        _check(self)
        self.users.remove(user)
        if not self.users:
            channels.remove(self)






