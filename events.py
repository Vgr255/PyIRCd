_events = {}

def set(event):
    assert isinstance(event, bytes), "event must be a byte string"
    assert event not in _events, "event may not already exist"
    assert event.isupper(), "event must be uppercase"
    def _setter(f):
        _events[event] = f
        return f
    return _setter

def get(serv, user, data):
    cmd, *rest = data.split()
    if cmd in _events:
        return _events[cmd](serv, user, rest)

    return _events[b"UNKNOWN COMMAND"](serv, cmd, user, rest)

@set(b"UNKNOWN COMMAND")
def unknown(serv, cmd, user, rest):
    serv.send(b"PRIVMSG", user, cmd, b":Unknown command")

