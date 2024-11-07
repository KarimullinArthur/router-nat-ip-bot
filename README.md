# Router NAT IP Bot

Small telegram bot, for send me my NAT router ip from node in LAN, via [UPnP IGD](https://en.wikipedia.org/wiki/Internet_Gateway_Device_Protocol).

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
[Already has systemd deamon](./contrib/router-nat-ip-bot.service)
And [.env](.env.tmp) tamplate 


### [Update message on channel](./src/update_channel_msg.py)
I think apscheduler and queues are bloated for this task. Instead, I would suggest using cron:

`(crontab -l ; echo "0 */24 * * * $(pwd)/venv/bin/python3 $(pwd)/src/update_channel_msg.py")| crontab -`


## Get IP from CLI
If your channel is public, you can get ip via [get_ip](./src/get_ip).
For example
```sh
ssh $(get_ip)
```

Don't forget rename [.env.tmp](./.env.tmp)
```
mv ./env.tmp .env
```
and add [channel_url in .env](./.env:L4)

#### PyInstaller

If you don't want store venv, you can build pyinstaller file
```sh
source venv/bin/activate && \
pyinstaller ./contrib/update_channel_msg.spec && \
sudo mv ./dist/update_channel_msg /usr/bin
```

If you don't want to place the .env file, edit [`update_channel_msg.py`](./src/update_channel_msg.py#L13)

Then with cron it would looking like this
`(crontab -l ; echo "0 */24 * * *  cd $(pwd) && update_channel_msg")| crontab -`

If you have edited the path of script or .env file, don't forget to edit the path in the crontab.

Also you can build the get-ip.py
```sh
source venv/bin/activate && \
pyinstaller ./contrib/get_ip.spec && \
sudo mv ./dist/getip /usr/bin
```

And also [to hardcode](./src/get_ip.py#L11) config data.

From 
```python
CHANNEL_URL = os.getenv("CHANNEL_URL")
```

To
```python
CHANNEL_URL = "https://t.me/username_your_channel/id_your_message" 
```

And rebuild.
