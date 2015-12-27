import itertools

import channels
import events

_maxparams = {

    b"JOIN": 2,
    b"PART": 2,
    b"QUIT": 1,
    b"MODE": 2,
    b"PRIVMSG": 2,

}

@events.set(b"JOIN")
def channel_join(serv, user, data):
    if data:
        channels, *rest = data.split()
    else:
        channels = rest = "" # rest is only needed for the check below; it will be false

    if rest:
        keys, *rest = rest
    else:
        keys = ""

    for chan, key in itertools.zip_longest(channels.split(","), keys.split(",")):
        pass















