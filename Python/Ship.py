from Vehicle import Vehicle

# class for ship
class Ship(Vehicle):
    
    # constructor
    def __init__(self, countryOfManufacture = ""):
        self.countryOfManufacture = countryOfManufacture
  
    # methods set and get for country manufacture attribute    
    def setCountryOfManufacture(self, countryOfManufacture):
        self.countryOfManufacture = countryOfManufacture
    
    def getCountryOfManufacture(self):
        return self.countryOfManufacture

     # methods for print the data
    def PrintData(self):
        print("Name                     : " + self.getModelName())
        print("Type                     : " + self.getType())
        print("Age                      : " + str(self.getAge()))
        print("Fuel Type                : " + self.getFuelType())
        print("Max Passengers           : " + str(self.getMaxPassengers()))
        print("Country of Manufacture   : " + self.countryOfManufacture)
        self.moveFunction()