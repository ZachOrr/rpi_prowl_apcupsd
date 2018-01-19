# APC Monitoring on Raspberry Pi with Prowl

A few scrips I use to monitor the status of my APC Back-UPS RS1000G with a Raspberry Pi. I use [Prowl](https://www.prowlapp.com/) to send notifications to my phone to alert me of changes

![](https://github.com/ZachOrr/rpi_prowl_apcupsd/blob/master/demo.jpg)

## Setup
 
Ensure Python is installed on your Raspberry Pi. Setup `apcupsd` on your Raspberry Pi [following these instructions](http://www.anites.com/2013/09/monitoring-ups.html). 

Clone and install `prowlpy` to use on your system

```
$ git clone https://github.com/jacobb/prowlpy
$ cd prowlpy
$ sudo python setup.py install
```

Clone and install `rpi_prowl_apcupsd` on your Pi

```
$ git clone https://github.com/ZachOrr/rpi_prowl_apcupsd.git
$ cd rpi_prowl_apcupsd
$ sudo python install.py
```

Modify `apcupsd.service` to setup environment variables with your Prowl API key

```
$ sudo nano /lib/systemd/system/apcupsd.service

[Unit]
Description=UPS power management daemon
Documentation=man:apcupsd(8)

[Service]
Environment='PROWL_API={YOUR_KEY_HERE}'
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