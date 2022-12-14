from time import sleep
import serial
from curses import ascii

"""
Run this file in your shell, the aim for this script is to try and allow you to
send, read and delete messages from python, after playing around with this for a while i have
realised that the most importain thing is good signal strength at the modem. For a full list of
fuctions that a GSM modem is capable of google Haynes AT+ commands

I have put the sleep function into many of the functions found within this script as it give the modem time
to receive all the messages from the Mobile Network Operators servers
"""

##set serial
ser = serial.Serial()

##Set port connection to USB port GSM modem
# ser.port = '/dev/tty.HUAWEIMobile-Pcui'
ser.port = "/dev/ttys007"

## set older phones to a baudrate of 9600 and new phones and 3G modems to 115200
ser.baudrate = 9600
# ser.baudrate = 115200
ser.rtscts = True
ser.dsrdtr = True
ser.timeout = 1
ser.open()
# chacommand = 'AT+CMGF=1\r\n'
# sleep(2)
# ser.write(chacommand.encode())
##following line of code sets the prefered message storage area to modem memory
# ser.write('AT+CPMS="ME","SM","ME"\r\n')


## Important understand the difference between PDU and text mode, in PDU istructions are sent to the port as numbers eg: 0,1,2,3,4 and in TEXT mode as text eg: "ALL", "REC READ" etc
## following line sets port into text mode, all instructions have to be sent to port as text not number
##Important positive responses from the modem are always returned as OK

##you may want to set a sleep timer between sending texts of a few seconds to help the system process


def sendsms(number, text):
    ser.write("AT+CMGF=1\r\n".encode())
    sleep(2)
    chanum = "AT+CMGS=" + number + "\r\n"
    ser.write(chanum.encode())
    sleep(2)
    ser.write(text.encode())
    sleep(2)
    ser.write(ascii.ctrl("z").encode())
    print("Text: %s  \nhas been sent to: %s" % (text, number))


def read_all_sms():
    ser.write("AT+CMGF=1\r\n".encode())
    sleep(5)
    ser.write('AT+CMGL="ALL"\r\n'.encode())
    sleep(15)
    a = ser.readlines()
    z = []
    y = []
    for x in a:
        if x.startswith("+CMGL:"):
            r = a.index(x)
            t = r + 1
            z.append(r)
            z.append(t)
    for x in z:
        y.append(a[x])

    ## following line changes modem back to PDU mode
    ser.write("AT+CMGF=0\r\n".encode())
    return y


def read_unread_sms():
    ser.write("AT+CMGF=1\r\n".encode())
    sleep(5)
    ser.write('AT+CMGL="REC UNREAD"\r\n'.encode())
    sleep(15)
    a = ser.readlines()
    z = []
    y = []
    for x in a:
        if x.startswith("+CMGL:"):
            r = a.index(x)
            t = r + 1
            z.append(r)
            z.append(t)
    for x in z:
        y.append(a[x])

    ##Following line changed modem back to PDU mode
    ser.write("AT+CMGF=0\r\n".encode())
    return y


def read_read_sms():
    ##returns all unread sms's on your sim card
    ser.write("AT+CMGS=1\r\n".encode())
    ser.read(100)
    ser.write('AT+CMGL="REC READ"\r\n'.encode())
    ser.read(1)
    a = ser.readlines()
    print("A:", a)
    for x in a:
        print(x)


def delete_all_sms():
    ##this changes modem back into PDU mode and deletes all texts then changes modem back into text mode
    ser.write("AT+CMGF=0\r\n".encode())
    sleep(5)
    ser.write("AT+CMGD=0,4\r\n".encode())
    sleep(5)
    ser.write("AT+CMGF=1\r\n".encode())


def delete_read_sms():
    ##this changes modem back into PDU mode and deletes read texts then changes modem back into text mode
    ser.write("AT+CMGF=0\r\n".encode())
    sleep(5)
    ser.write("AT+CMGD=0,1\r\n".encode())
    sleep(5)
    ser.write("AT+CMGF=1\r\n".encode())


##this is an attempt to run ussd commands from the gsm modem


def check_ussd_support():
    ##if return from this is "OK" this phone line supports USSD, find out the network operators codes
    ser.write("AT+CMGF=0\r\n".encode())
    ser.write("AT+CUSD=?\r\n".encode())
    ser.write("AT+CMGF=1\r\n".encode())


##This function is an attempt to get your sim airtime balance using USSD mode
def get_balance():
    ##first set the modem to PDU mode, then pass the USSD command(CUSD)=1, USSD code eg:*141# (check your mobile operators USSD numbers)
    ## Error may read +CUSD: 0,"The service you requested is currently not available.",15
    ## default value for <dcs> is 15 NOT 1
    ser.write("AT+CMGF=0\r\n".encode())
    ser.write("AT+CUSD=1,*600#,15\r\n".encode())
    ser.read(1)
    a = ser.readlines()
    print(a)
    ser.write("AT+CMGF=1\r\n".encode())


def ussd_sms_check():
    ##first set the modem to PDU mode, then pass the USSD command(CUSD)=1, USSD code eg:*141# (check your mobile operators USSD numbers)
    ser.write("AT+CMGF=0\r\n".encode())
    ser.write("AT+CUSD=1,*141*1#,15\r\n".encode())
    ser.read(100)
    a = ser.readlines()
    print(a)
    ser.write("AT+CMGF=1\r\n".encode())


read_read_sms()
# sendsms('0998006237','test yo')
# get_balance()
# read_read_sms()
# check_ussd_support()
