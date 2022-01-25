Before you begin, install digi-xbee using: 

`pip install digi-xbee` or `pip3 install digi-xbee`



Note: OTA FIRMWARE UPDATE functionality (not used in this utility) requires digi-xbee package v1.4.3 or later. If the official digi-xbee package is not yet v1.4.3, then use: 

`pip install digi-xbee-unofficial` or `pip3 install digi-xbee-unofficial`


How to install / run:

- log in as gateway user (or any user with sudo privileges)
- enter `sudo su` then enter gateway user password
- enter `git clone https://github.com/gregcompton/xbeeBasicListener.git`
- enter `cd xbeeBasicListener`
- enter `pip install digi-xbee`
- enter `pip install pyserial`
- run `python main.py` if you get an error here, run `python3 main.py`