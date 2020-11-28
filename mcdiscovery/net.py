import socket
from threading import Thread
from typing import List
import struct

from .types import LocalServer
from .metadata import convertUDPStringToServerInfo

# Address used by Minecraft to announce itself
_MC_MULTICAST_ADDRESS = "224.0.2.60"
_MC_MULTICAST_PORT = 4445


class LANServerFinder(Thread):
    """Class that finds Minecraft LAN servers on the local network"""

    # Net
    _sock: socket.socket

    # Meta
    _running: bool = True

    # Server lists
    _known_servers: List[LocalServer] = []
    _known_server_hashes: List[int] = []

    def __init__(self):
        super().__init__()

    def run(self):

        # Open the socket
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.bind(("0.0.0.0", _MC_MULTICAST_PORT))

        # Add the socket to the multicast group
        group = socket.inet_aton(_MC_MULTICAST_ADDRESS)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self._sock.setsockopt(
            socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        # Listen for messages
        while self._running:

            # Capture packet
            data, address = self._sock.recvfrom(1024)

            # Parse data
            info = convertUDPStringToServerInfo(data.decode(), address[0])

            # If this server is unknown, track it
            if hash(info) not in self._known_server_hashes:
                self._known_servers.append(info)
                self._known_server_hashes.append(hash(info))

    def stop(self):
        self._running = False

    def start(self):
        self._running = True
        super().start()

    def getAllFoundServers(self) -> List[LocalServer]:
        return self._known_servers
