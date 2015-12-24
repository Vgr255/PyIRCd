_events = {}

def set(event):
    assert isinstance(event, bytes), "event must be a byte string"
    assert event not in _events, "event may not already exist"
    assert event.isupper(), "event must be uppercase"
    def _setter(f):
        _events[event] = f
        return f
    return _setter

def get(data):
    cmd, *rest = data
    if cmd in _events:
        _events[cmd](*rest[_maxparams[cmd]:])





