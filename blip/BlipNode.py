class BlipNode():
    def __init__ (self, title, blipConnection): 
        self.title = title
        self.blipConnection = blipConnection
        self.blipConnection = []
        
    def __str__(self):
        return f"{self.title}"
    
    # connect will add blips into the intial blipConnection list
    def connect (self, blip):
        self.blipConnection.append(blip.title)
        
    # showConnection will display the list of blipConnections for the intial blip object
    def showConnection(self): 
        print("Connection:  " , self.blipConnection)
        
    
# dC - Dual connection connects two nodes through two way connection. Only establishes a single, bidirectional connection
def dC(b1, b2): 
   
    
    if(b2.title in b1.blipConnection or b1.title in b2.blipConnection): 
        print("Already Connected to blip")
    else: 
        b1.connect(b2)
        b2.connect(b1)
