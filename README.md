# Router NAT IP Bot

Small telegram bot, for send me my NAT router ip from node in LAN.
## Install
### Dependencies
* miniupnpc

Install on Debian-based
`sudo apt install miniupnpc`

If in your repo old version miniupnpc, and it doesn't work, try build it from source:
```sh
VERSION=2.2.8
wget http://miniupnp.free.fr/files/miniupnpc-$VERSION.tar.gz
tar -xvf miniupnpc-$VERSION.tar.gz && cd miniupnpc-$VERSION
make install
```

### [Bot](./src/bot.py)
[Already systemd deamon](./extra/router-nat-ip-bot.service)

### [Update message on channel](./src/update_channel_msg.py)
I think apscheduler and queues are bloated for this task. Instead, I would suggest using cron:

`(crontab -l ; echo "0 */24 * * * $(pwd)/venv/bin/python3 $(pwd)/src/update_channel_msg.py")| crontab -`

#### PyInstaller

If you don't want store venv, you can build pyinstaller file
```sh
source venv/bin/activate && \
pyinstaller ./extra/update_channel_msg.spec && \
sudo mv ./dist/update_channel_msg /usr/bin
```

If you don't want to place the .env file, edit [`update_channel_msg.py`](./src/update_channel_msg.py#L12-L14)

Then with cron it would looking like this

`(crontab -l ; echo "0 */24 * * *  cd $(pwd) && update_channel_msg")| crontab -`

If you have edited the path of script or .env file, don't forget to edit the path in the crontab.
