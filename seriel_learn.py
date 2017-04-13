import serial.tools.list_ports
import serial
import time
from threading import Thread

port_list = serial.tools.list_ports.comports()
port_list = [each.device for each in port_list]
print(port_list)
serial1 = serial.Serial(
    port='com9',
    baudrate=9600
)


# print(serial1)

# serial1.open()

def rx():
    while 1:
        time.sleep(0.1)
        n = serial1.inWaiting()
        if n > 0:
            print(n)
            data = serial1.read(n)
            print(data)


def rx_thread():
    t = Thread(name="rx", target=rx)
    t.start()


cnt = 0
rx_thread()
while 1:
    s=input()
    if len(s)>0:
        # 不知道为什么这里要加上\r\n才能正常地返回
        s+='\r\n'
        data=s.encode()
        print(serial1.write(data))
