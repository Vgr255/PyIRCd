import itertools

import channels
import events

@events.set(b"JOIN")
def channel_join(serv, user, data):
    if data:
        channels, *rest = data.split()
    else:
        channels = []

    if rest:
        keys, *rest = rest
    else:
        keys = []

    for chan, key in itertools.zip_longest(channels.split(","), keys.split(",")):
        pass















