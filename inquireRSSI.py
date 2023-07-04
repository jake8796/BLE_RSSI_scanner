from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            if dev.getValueText(9) != "None":
                print("Discovered device:", dev.addr)
                print("Device description:", dev.getValueText(9))  # Printing Device Description (Complete Local Name)

        if isNewData:
            print("RSSI:", dev.rssi)


scanner = Scanner().withDelegate(ScanDelegate())

while True:
    devices = scanner.scan(5)  # Scans for 5 seconds