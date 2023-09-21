# APC Monitoring on Raspberry Pi with Prowl

A few scripts originally written by [Zach0rr](https://github.com/ZachOrr/rpi_prowl_apcupsd), which I have modified to use apprise instead of prowl. These get apcupsd to send push notifications e.g when mains power goes off.

![](https://github.com/alistairporter/apprise_apcupsd/blob/master/demo.jpg)

## Setup
 
Ensure Python is installed on your Raspberry Pi. Setup `apcupsd` on your Raspberry Pi [following these instructions](http://www.anites.com/2013/09/monitoring-ups.html). 

Clone and install `apprise` to use on your system either using pip with 

`pip install apprise`
Alternatively using the system package manager, e.g on debian/ubuntu

`sudo apt install apprise` 

Clone and install `apprise_apcupsd` on your Pi

```
$ git clone https://github.com/alistairporter/apprise_apcupsd.git
$ cd apprise_apcupsd
$ sudo python install.py
```

Modify `apcupsd.service` to setup environment variables with your apprise uri

```
$ sudo nano /lib/systemd/system/apcupsd.service

[Unit]
Description=UPS power management daemon
Documentation=man:apcupsd(8)

[Service]
Environment='APPRISE_URI={YOUR_URI_HERE}'
ExecStartPre=/lib/apcupsd/prestart
ExecStart=/sbin/apcupsd -f /etc/apcupsd/apcupsd.conf
Type=forking
KillMode=process
PIDFile=/var/run/apcupsd.pid

[Install]
WantedBy=multi-user.target
```

Reload `systemctl` and restart `apcupsd.service`

```
$ sudo systemctl daemon-reload
$ sudo systemctl restart apcupsd.service
```
