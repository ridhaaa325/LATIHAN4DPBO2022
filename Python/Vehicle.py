# class for vehicle
class Vehicle:
    
    # constructor
    def __init__(self, modelName = "", fuelType = "", maxPassenger = 0, age = 0, tipe = ""):
        self.modelName = modelName
        self.fuelType = fuelType
        self.maxPassengers = maxPassenger
        self.age = age
        self.type = tipe
    
    # methods set and get for model name attribute
    def setModelName(self, modelName):
        self.modelName = modelName
    
    def getModelName(self):
        return self.modelName
    
    # methods set and get for fuel type attribute
    def setFuelType(self, fuelType):
        self.fuelType = fuelType
    
    def getFuelType(self):
        return self.fuelType

    # methods set and get for max passangers attribute
    def setMaxPassengers(self, maxPassengers):
        self.maxPassengers = maxPassengers
    
    def getMaxPassengers(self):
        return self.maxPassengers
    
    # methods set and get for age attribute
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age
    
    # methods set and get for type attribute
    def setType(self, tipe):
        self.type = tipe
    
    def getType(self):
        return self.type
    
    # move method 
    def moveFunction(self):
        print(self.modelName + " is moving.")