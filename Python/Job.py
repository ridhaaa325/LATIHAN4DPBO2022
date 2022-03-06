# class for job
class Job:
    
    # constructor
    def __init__(self, nip = "", companyName = "", position = ""):
        self.nip = nip
        self.companyName = companyName
        self.position = position
    
    # methods set and get for NIP attribute
    def setNIP(self, nip):
        self.nip = nip
    
    def getNIP(self):
        return self.nip
    
    # methods set and get for company name attribute
    def setCompanyName(self, companyName):
        self.companyName = companyName
    
    def getCompanyName(self):
        return self.companyName
    
    # methods set and get for position attribute
    def setPosition(self, position):
        self.position = position
    
    def getPosition(self):
        return self.position