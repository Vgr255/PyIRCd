import config

def parse_raw_data(data):
    assert isinstance(data, bytes), "data must be bytes"
    cmd, *rest = data.split(b" ")
    args = [cmd.upper()]
    for i, arg in enumerate(rest):
        if arg.startswith(b":"):
            args.append(b" ".join([arg[1:]] + rest[i+1:]))
            break

        args.append(arg)

    return args




