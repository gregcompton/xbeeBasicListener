import json
from sys import platform
from datetime import datetime

try:
    from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress
except Exception as e:
    print(e)
    print("install digi-xbee using: pip install digi-xbee or pip3 install digi-xbee\n")
    print("--------------------------")
    print("OTA FIRMWARE UPDATE functionality requires package v1.4.3 or later. ")
    print("if the official digi-xbee package is not yet v1.4.3, pip install digi-xbee-unofficial")
    libraries = False


if platform.startswith('win'):
    port = "COM15"  # todo: change the the correct port number for your windows machine
else:
    port = "/dev/ttyUSB0"
baud_rate = 9600
local_xbee = XBeeDevice(port, baud_rate)


def handle_rx_packet(xbee_message):
    print("----------------------------------")

    remote_address = xbee_message.remote_device.get_64bit_addr()
    timestamp = xbee_message.timestamp
    payload = xbee_message.data.decode()

    print("RECEIVED from %s (String)>> %s >> %s" % (
        remote_address, str(datetime.fromtimestamp(timestamp)),
        payload))


def select_comm_port(device_name):
    import serial.tools.list_ports  # from pyserial
    list = serial.tools.list_ports.comports()

    print('\nSelect the number corresponding to the %s  com port:' % device_name)
    for p in list:
        if p[1][:3] == 'USB':
            print(list.index(p), ' -> ', p[0])
    x = int(input())

    return list[x][0]


def main():
    print("STARTING BASIC XBEE LISTENER UTILITY")

    
    try:
        print('Attempting to open local_xbee on default port: ', port)
        local_xbee.open()
        print("Success! local_xbee open on port: ", port)
    except Exception as e:
        print("Can't open local_xbee on port: ", port)
        cport = select_comm_port('local_xbee')
        local_xbee = XBeeDevice(cport, baud_rate)
        try:
            print('Trying to open local_xbee on port: ', cport)
            local_xbee.open()
            print("SUCCESS on port: ", cport)
        except Exception as e:
            print('FAILED (local_xbee): ', e)
            print('Please check your connections and try again. Hint: use XCTU to identify correct ports')
            sys.exit(9)

    local_xbee.add_data_received_callback(handle_rx_packet)

    print("Press ctrl-C (command-C on Mac) at any time to quit the program")
    print("Waiting for data...")

    while True:
        pass

main()