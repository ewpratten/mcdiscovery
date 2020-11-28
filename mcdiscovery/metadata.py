import re

from .types import LocalServer

_SERVER_PORT_PATTERN = r"\[AD\]([0-9]*)\[\/AD\]"
_SERVER_MOTD_PATTERN = r"\[MOTD\](.*)\[\/MOTD\]"


def convertUDPStringToServerInfo(udp_str: str, server_ip: str) -> LocalServer:
    """Converts a Minecraft LAN broadcast metadata string to a LocalServer object.

    This function operates as per: https://github.com/tomsik68/mclauncher-api/blob/master/src/main/java/sk/tomsik68/mclauncher/impl/servers/VanillaServerFinder.java#L22

    Args:
        udp_str (str): Raw metadata string
        server_ip (str): IP of the origionating server

    Returns:
        LocalServer: Server metadata object
    """

    # RE parse
    port = re.findall(_SERVER_PORT_PATTERN, udp_str, re.M)[0]
    motd = re.findall(_SERVER_MOTD_PATTERN, udp_str, re.M)[0]

    # Construct and return obj
    return LocalServer(server_ip, int(port), motd)
