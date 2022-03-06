from Job import Job

# class for driver
class Driver(Job):
    
    # constructor
    def __init__(self, licenseId = "", activeUntil = "", vehicleType = ""):
        self.licenseId = licenseId
        self.activeUntil = activeUntil
        self.vehicleType = vehicleType

    # methods set and get for license attribute
    def setLicenseID(self, licenseId):
        self.licenseId = licenseId
        
    def getLicenseID(self):
        return self.licenseId
    
    def setActiveID(self, activeUntil):
        self.activeUntil = activeUntil
        
    def getActiveID(self):
        return self.activeUntil
    
    # methods set and get for vehicle type attribute
    def setVehicleType(self, vehicleType):
        self.vehicleType = vehicleType
    
    def getVehicleType(self):
        return self.vehicleType