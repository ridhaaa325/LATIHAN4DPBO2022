from Driver import Driver

# class for person
class Person:
    
    # constructor
    def __init__(self, nik = "", name = "", gender = "", driver = Driver()):
        self.nik = nik
        self.name = name
        self.gender = gender
        self.driver = driver
    
    # methods set and get for NIK attribute
    def setNIK(self, nik):
        self.nik = nik
    
    def getNIK(self):
        return self.nik
    
    # methods set and get for name attribute
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    # methods set and get for gender attribute
    def setGender(self, gender):
        self.gender = gender
    
    def getGender(self):
        return self.gender

    # methods set and get for driver attribute
    def setDriver(self, driver):
        self.driver = driver
    
    def getDriver(self):
        return self.driver
    
    def sleepFunction(self):
        print(self.name + " is sleeping.")
    
    # methods for print the data
    def PrintData(self):
        print("NIK              : " + self.nik)
        print("Name             : " + self.name)
        print("Gender           : " + self.gender)
        print("Driver License   : " + self.driver.getLicenseID())
        print("Active Until     : " + self.driver.getActiveID())
        print("Vehicle Type     : " + self.driver.getVehicleType())
        print("NIP              : " + self.driver.getNIP())
        print("Company Name     : " + self.driver.getCompanyName())
        print("Position         : " + self.driver.getPosition())
        self.sleepFunction()