# Status: Fully working so far

import re

import config

_prefix_match = re.compile("^:.+!.+@.+$").match

def parse_raw_data(data):
    params = data.split(b" ")
    if _prefix_match(params[0]): # prefix; ignore
        _, cmd, *rest = params
    else:
        cmd, *rest = params
    args = [cmd.upper()]
    for i, arg in enumerate(rest):
        if arg.startswith(b":"):
            args.append(b" ".join([arg[1:]] + rest[i+1:]))
            break

        args.append(arg)

    return args
