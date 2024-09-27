Small telegram bot, for send me my nat router ip from node in LAN.

Dependencies:
* miniupnpc

Install on Debian-based
`sudo apt install miniupnpc`

If in your repo old version miniupnpc, and it doesn't work, try build it from source:
```
VERSION=2.2.8
wget http://miniupnp.free.fr/files/miniupnpc-$VERSION.tar.gz
tar -xvf miniupnpc-$VERSION.tar.gz && cd miniupnpc-$VERSION
make install
```
