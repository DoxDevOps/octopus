import os
import serial
import time


class TextMessage:
    def __init__(
        self,
        recipient=os.environ.get("INBOUND_SMS_SHORT_CODE", "0999111222"),
        message="TextMessage.content not set.",
    ):
        self.recipient = recipient
        self.content = message

    def set_recipient(self, number):
        self.recipient = number

    def set_content(self, message):
        self.content = message

    def connect_phone(self):
        # [TODO] Need to remove hard-coded device path
        self.ser = serial.Serial("/dev/ttyUSB0", 460800, timeout=5)
        time.sleep(1)

    def send_message(self):
        self.ser.write("ATZ\r")
        time.sleep(1)
        self.ser.write("AT+CMGF=1\r")
        time.sleep(1)
        self.ser.write('''AT+CMGS="''' + self.recipient + """"\r""")
        time.sleep(1)
        self.ser.write(self.content + "\r")
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)

    def disconnect_phone(self):
        self.ser.close()
