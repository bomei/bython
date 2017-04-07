import serial
import serial.tools.list_ports

plist=serial.tools.list_ports.comports()
print(1)
for each in plist:
    print(each)