from Vehicle import Vehicle

# class for airplane
class Airplane(Vehicle):
    
    # constructor
    def __init__(self, wingType = "", engineModel = ""):
        self.wingType = wingType
        self.engineModel = engineModel
        
    # methods set and get for wing type attribute
    def setWingType(self, wingType):
        self.wingType = wingType
    
    def getWingType(self):
        return self.wingType
    
    # methods set and get for engine model attribute
    def setEngineModel(self, engineModel):
        self.engineModel = engineModel
        
    def getEngineModel(self):
        return self.engineModel
    
    # methods for print the data
    def PrintData(self):
        print("Name             : " + self.getModelName())
        print("Type             : " + self.getType())
        print("Age              : " + str(self.getAge()))
        print("Fuel Type        : " + self.getFuelType())
        print("Wings Type       : " + self.wingType)
        print("Engine Model     : " + str(self.engineModel))
        print("Max Passengers   : " + str(self.getMaxPassengers()))
        self.moveFunction()