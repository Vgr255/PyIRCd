# Offline tests

import unittest

import parse

class IRCServerTest(unittest.TestCase):
    def test_parse_raw_data(self):
        with self.assertRaises(AssertionError):
            parse.parse_raw_data("non-byte object")

        data = [
            (b"JOIN :#channel", [b"JOIN", b"#channel"]),
            (b"PRIVMSG target :message", [b"PRIVMSG", b"target", b"message"]),
            (b"QUIT", [b"QUIT"]),
            (b"QUIT :", [b"QUIT", b""]),
            (b"PRIVMSG target : multi spaced     message    ", [b"PRIVMSG", b"target", b" multi spaced     message    "]),
        ]

        for in_data, expected in data:
            result = parse.parse_raw_data(in_data)
            self.assertEqual(result, expected)
















unittest.main()
