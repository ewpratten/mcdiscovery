from . import *
import time


def main():

    # Set up a server finder
    finder = LANServerFinder()

    # Start looking for Minecraft servers
    finder.start()

    # Track the most recent server index
    latest_idx = 0

    # Run logger
    print("Listening for local Minecraft servers. Press CTRL+C to stop")
    try:
        while True:
            
            # Check for new data
            known_servers = finder.getAllFoundServers()
            if len(known_servers) > latest_idx:
                
                # Get the server info
                info = known_servers[latest_idx]
                latest_idx += 1
                
                # Log the server
                print(f"Found new LAN server hosted by {info.address}:{info.port} MOTD: \"{info.motd}\"")
            

    except KeyboardInterrupt as e:
        print("Closing sockets")
        finder.stop()
        finder.join()
        return 0


if __name__ == "__main__":
    exit(main())
