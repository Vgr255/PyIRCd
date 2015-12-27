# Status: Nonfunctional WIP

import types

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

    modes_match = types.MappingProxyType({

        "i": "invite_only",
        "k": "key",
        "j": "throttle",
        "l": "limit",
        "f": "forward",
        "n": "no_extmsgs",
        "t": "topic_opsonly",
        "s": "secret",
        "p": "private",
        "m": "moderated",
        "r": "registered_only",
        "c": "no_colors",
        "g": "free_invite",
        "z": "op_moderated",
        "L": "large_lists",
        "P": "permanent",
        "F": "free_target",
        "Q": "no_forward",
        "C": "no_ctcp",
        "o": "ops",
        "v": "voices",
        "b": "bans",
        "q": "quiets",
        "e": "exempts",
        "I": "invites",

    })

    _invite_only = False
    _key = None
    _throttle = None
    _limit = None
    _forward = None
    _no_extmsgs = False
    _topic_opsonly = False
    _secret = False
    _private = False
    _moderated = False
    _registered_only = False
    _no_colors = False
    _free_invite = False
    _op_moderated = False
    _larger_lists = False
    _permanent = False
    _free_target = False
    _no_forward = False
    _no_ctcp = False

    def __init__(self, name):
        self.name = name
        self._users = set()
        self._modes = set()
        self._displayed_modes = set()
        self._ops = set()
        self._voices = set()
        self._bans = set()
        self._quiets = set()
        self._exempts = set()
        self._invites = set()

    def check_modes(self):
        to_add = self._modes - self._displayed_modes
        to_rem = self._displayed_modes - self._modes

    @property
    def modes(self):
        return set(self._modes)

    @property
    def invite_only(self):
        return self._invite_only

    @invite_only.setter
    def invite_only(self, value):
        if not value and self._invite_only:
            self._modes.remove("i")
            self._invite_only = False
        elif value and not self._invite_only:
            self._modes.add("i")
            self._invite_only = True

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        if self._key is None and value is not None:
            self._modes.add("k")
            self._key = value
        elif self._key is not None:
            if value is None:
                self._modes.remove("k")
            self._key = value

    @property
    def throttle(self):
        return self._throttle

    @throttle.setter
    def throttle(self, value):
        if self._throttle is None and value is not None:
            self._modes.add("j")
            self._throttle = int(value)
        elif self._throttle is not None:
            if value is None:
                self._modes.remove("j")
                self._throttle = None
            else:
                self._throttle = int(value)

    def join(self, user, key):
        self.users[user.name] = user

    def part(self, data):
        self.users.remove(user)
        if not self.users and not self.permanent:
            del _channels[self.name]

    def quit(self, data):
        pass

    def mode(self, user, target, modes):
        pass


