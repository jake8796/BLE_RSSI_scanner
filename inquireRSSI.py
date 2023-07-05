from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            if dev.getValueText(9) != "None":
                pass
                #print("Discovered device:", dev.addr)
                #print("Device description:", dev.getValueText(9))  # Printing Device Description (Complete Local Name)

        if isNewData:
            pass
            #print("RSSI:", dev.rssi)


scanner = Scanner().withDelegate(ScanDelegate())

while True:
    devices = scanner.scan(0.1)  # Scans for 500 mS
    for dev in devices:
        if dev.getValueText(9) == 'Test Device': #Get Device description
            print (" Device: ",str(dev.addr)," RSSI: ",str(dev.rssi)," Device description:", dev.getValueText(9))
