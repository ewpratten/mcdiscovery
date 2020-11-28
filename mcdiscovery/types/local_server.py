class LocalServer(object):
    """Information about a Minecraft LAN server"""

    address: str
    port: int
    motd: str

    def __init__(self, address: str, port: int, motd: str):
        """Create a LocalServer object

        Args:
            address (str): Server IPv4 address
            port (int): Server port
            motd (str): Server MOTD
        """

        self.address = address
        self.port = port
        self.motd = motd
        
    def __hash__(self):
        return hash((self.address, self.port, self.motd))