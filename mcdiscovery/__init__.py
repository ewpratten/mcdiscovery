import socket
import re

class LocalServer(object):
    address: str
    port: int
    motd: str

