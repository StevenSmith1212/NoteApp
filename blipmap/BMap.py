class BMap:
    def __init__(self, mapConn):
        self.mapConn = mapConn
        mapConn = []
        
    def addBlip(self, blip):
        self.mapConn.append(blip.title)
        
    def showMap(self):
        print(self.mapConn)
        

