from mcdiscovery.metadata import *


def test_convertUDPStringToServerInfo():

    udp_str = "[AD]54345[/AD][MOTD]Tomsik68's world[/MOTD]"
    addr = "172.0.0.1"

    # Parse
    output = convertUDPStringToServerInfo(udp_str, addr)

    # Check values
    assert output.address is addr
    assert output.motd == "Tomsik68's world"
    assert output.port == 54345
