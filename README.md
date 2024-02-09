# raspberrypi-telegrambot-frame

Transform your Raspberry Pi into a smart PhotoFrame! My project integrates a Telegram bot for easy photo uploads. Enjoy automated retrieval, customizable display, and remote control. Prioritize security and join me for ongoing enhancements. Share memories effortlessly!

![___](https://github.com/orest0/raspberrypi-telegrambot-frame/assets/15201969/f5dc8739-d76e-4640-9237-8c4b39702765)

## MANUAL INSTALLATION

If you want to build the photoframe, here's how to get started:

1. Open CMD and paste commands:

        sudo apt-get update
        sudo apt-get upgrade
        sudo apt-get install feh
        pip install python-telegram-bot==13.7 -break-system-packages

2. Then enter these commands

        cd
        git clone https://github.com/orest0/raspberrypi-telegrambot-frame.git
        cd raspberrypi-telegrambot-frame/Teleframe
        nano bot.py

!!ADD YOUR TELEGRAM BOT TOKEN!! in the 5-th line

<img width="480" alt="ADD_BOT_TOKEN" src="https://github.com/orest0/raspberrypi-telegrambot-frame/assets/15201969/0772ab1c-2931-471b-b400-1dbc9612edeb">

3. Change Save and Close

Ctrl+X
Y
Enter

4. Create bot service

        sudo nano /etc/systemd/system/bot.service

5. Add this to the file

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


6. Change Save and Close

Ctrl+X
Y
Enter

7. Enable the service

        sudo systemctl enable bot
        sudo systemctl start bot

!!UPLOAD THE FIRST PHOTO AND CHECK FOR A REPLY!!

8. Create a frame service

        sudo nano /etc/systemd/system/frame.service

9. Add this to the file

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

10. Change Save and Close

Ctrl+X
Y
Enter

11. Enable the service

        sudo systemctl enable frame
        sudo systemctl start frame

12. Disable cursor

        sudo apt-get install unclutter
        nano ~/.config/lxsession/LXDE-pi/autostart

13. Add this to the file

        @unclutter -idle 0
        @xset s noblank
        @xset s off
        @xset -dpms

14. Change Save and Close

Ctrl+X
Y
Enter

15. Reboot and enjoy

        sudo reboot
