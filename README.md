# Minecraft LAN Server Discovery ![Poetry Test Suite](https://github.com/Ewpratten/mcdiscovery/workflows/Poetry%20Test%20Suite/badge.svg) ![Poetry Build Suite](https://github.com/Ewpratten/mcdiscovery/workflows/Poetry%20Build%20Suite/badge.svg) [![PyPI version](https://img.shields.io/pypi/v/mcdiscovery.svg)](https://pypi.python.org/pypi/mcdiscovery/)

`mcdiscovery` is a Python library and CLI tool for discovering Minecraft LAN worlds / servers on your local network. This works in accordance to [@tomsik68](https://github.com/tomsik68)'s protocol description [here](https://github.com/tomsik68/mclauncher-api/wiki/LAN-Server-Discovery).

## Installation

To install, ensure your system has `python3` and `python3-pip`, then run:

```sh
python3 -m pip install mcdiscovery
```

## Usage

`mcdiscovery` can be used as a CLI tool by running `python3 -m mcdiscovery`, or as a library with `import mcdiscovery`. API documentation can be found [here](https://ewpratten.retrylife.ca/mcdiscovery/mcdiscovery.net.LANServerFinder.html). 