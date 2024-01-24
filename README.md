# raspberrypi-telegrambot-frame
Transform your Raspberry Pi into a smart PhotoFrame! Our project integrates a Telegram bot for easy photo uploads. Enjoy automated retrieval, customizable display, and remote control. Prioritize security and join our community for ongoing enhancements. Share memories effortlessly!

![___](https://github.com/orest0/raspberrypi-telegrambot-frame/assets/15201969/f5dc8739-d76e-4640-9237-8c4b39702765)

----MANUAL INSTALLATION----

Take all these steps in CMD to create the PhotoFrame:

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install feh

pip install python-telegram-bot==13.7 -break-system-packages

cd
git clone https://github.com/orest0/raspberrypi-telegrambot-frame.git
cd raspberrypi-telegrambot-frame/Teleframe
nano bot.py

<img width="480" alt="ADD_BOT_TOKEN" src="https://github.com/orest0/raspberrypi-telegrambot-frame/assets/15201969/0772ab1c-2931-471b-b400-1dbc9612edeb">

!!ADD YOUR TELEGRAM BOT TOKEN!! in 4-th lane

Ctrl+X
Y
Ctrl+C

sudo nano /etc/systemd/system/bot.service

____ADD THIS TO THE FILE____

[Unit]
Description=bot
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/pi/raspberrypi-telegrambot-frame/Teleframe/bot.py
Restart=always
RestartSec=10
User=pi

[Install]
WantedBy=multi-user.target

____________________________

Ctrl+X
Y
Ctrl+C

sudo systemctl enable bot
sudo systemctl start bot

!!UPLOAD FIRST PHOTO AND CHECK FOR REPLY!!

sudo nano /etc/systemd/system/frame.service

____ADD THIS TO THE FILE____

[Unit]
Description=frame
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/bash /home/pi/raspberrypi-telegrambot-frame/Teleframe/frame.sh
Restart=always
RestartSec=10
User=pi

[Install]
WantedBy=multi-user.target

____________________________

Ctrl+X
Y
Ctrl+C

sudo systemctl enable frame
sudo systemctl start frame

sudo apt-get install unclutter
nano ~/.config/lxsession/LXDE-pi/autostart

____ADD THIS TO THE FILE____

@unclutter -idle 0
@xset s noblank
@xset s off
@xset -dpms
____________________________

Ctrl+X
Y
Ctrl+C

sudo reboot




