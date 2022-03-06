# call the all class files.
from Job import Job
from Driver import Driver
from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane
from Person import Person

# input for person class
person = [Person("123451", "Ucup", "Man", Driver("A", "2022", "Car")), 
          Person("123452", "Udin", "Man", Driver("C", "2025", "Motorbike")), 
          Person("123453", "Michele", "Women", Driver("A", "2022", "Car")), 
          Person("123454", "Jasmine", "Women", Driver("PPL", "2024","Plane")), 
          Person("123455", "Mikaela", "Women", Driver("A", "2022","Car"))]

person[0].getDriver().setNIP("00001")
person[0].getDriver().setCompanyName("Pertamina")
person[0].getDriver().setPosition("Vice Chairman")

person[1].getDriver().setNIP("00002")
person[1].getDriver().setCompanyName("Telkom")
person[1].getDriver().setPosition("Human Resources")

person[2].getDriver().setNIP("00003")
person[2].getDriver().setCompanyName("Tokopedia")
person[2].getDriver().setPosition("Employee")

person[3].getDriver().setNIP("00004")
person[3].getDriver().setCompanyName("Emirates")
person[3].getDriver().setPosition("Employee")

person[4].getDriver().setNIP("00005")
person[4].getDriver().setCompanyName("Prestige Motor")
person[4].getDriver().setPosition("Employee")

print("-----------------------")
print("     Person Class ")
print("-----------------------")

for i in range(0,5):
    person[i].PrintData()
    print("\n")

# input for ship class
print("-----------------------")
print("     Ship Class ")
print("-----------------------")

ship1 = Ship()
ship1.setCountryOfManufacture("Indonesia")
ship1.setModelName("Strategic Sealift Vessel ")
ship1.setAge(10)
ship1.setFuelType("Solar")
ship1.setMaxPassengers(100)
ship1.setType("Container Ship")
ship1.PrintData()
print("\n")

ship2 = Ship()
ship2.setCountryOfManufacture("Singapore")
ship2.setModelName("Symphony of the Seas")
ship2.setAge(7)
ship2.setFuelType("Diesel")
ship2.setMaxPassengers(6687)
ship2.setType("Passanger Ship")
ship2.PrintData()
print("\n")

ship3 = Ship()
ship3.setCountryOfManufacture("Germany")
ship3.setModelName("Oasis of the Seas")
ship3.setAge(1)
ship3.setFuelType("Solar")
ship3.setMaxPassengers(6699)
ship3.setType("Passanger Ship")
ship3.PrintData()
print("\n")

ship4 = Ship()
ship4.setCountryOfManufacture("Netherland")
ship4.setModelName("Allure of the Seas")
ship4.setAge(5)
ship4.setFuelType("Diesel")
ship4.setMaxPassengers(6780)
ship4.setType("Passanger Ship")
ship4.PrintData()
print("\n")

ship5 = Ship()
ship5.setCountryOfManufacture("Russia")
ship5.setModelName("Iona")
ship5.setAge(3)
ship5.setFuelType("Biofuel")
ship5.setMaxPassengers(6600)
ship5.setType("Passanger Ship")
ship5.PrintData()
print("\n")

# input for airplane class
print("-----------------------")
print("     Airplane Class ")
print("-----------------------")

airplane1 = Airplane()
airplane1.setModelName("Antonov An - 225")
airplane1.setWingType("Fixed Wing")
airplane1.setEngineModel("Turbo")
airplane1.setAge(3)
airplane1.setMaxPassengers(300)
airplane1.setType("Passanger Airplane")
airplane1.setFuelType("Avtur")
airplane1.PrintData()
print("\n")

airplane2 = Airplane()
airplane2.setModelName("Airbus A320")
airplane2.setWingType("Low Wing")
airplane2.setEngineModel("Turbo")
airplane2.setAge(3)
airplane2.setMaxPassengers(180)
airplane2.setType("Passanger Airplane")
airplane2.setFuelType("Avtur")
airplane2.PrintData()
print("\n")

airplane3 = Airplane()
airplane3.setModelName("Cessna 172")
airplane3.setWingType("Fixed Wing")
airplane3.setEngineModel("Turbo")
airplane3.setAge(20)
airplane3.setMaxPassengers(4)
airplane3.setType("Private Airplane")
airplane3.setFuelType("100LL")
airplane3.PrintData()
print("\n")

airplane4 = Airplane()
airplane4.setModelName("Boeing 737")
airplane4.setWingType("Fixed Wing")
airplane4.setEngineModel("CFM International CFM56")
airplane4.setAge(5)
airplane4.setMaxPassengers(132)
airplane4.setType("Passanger Airplane")
airplane4.setFuelType("Avtur")
airplane4.PrintData()
print("\n")

airplane5 = Airplane()
airplane5.setModelName("Sukhoi SU-27")
airplane5.setWingType("Fixed Wing")
airplane5.setEngineModel("Supersonic")
airplane5.setAge(5)
airplane5.setMaxPassengers(132)
airplane5.setType("War Airplane")
airplane5.setFuelType("Avtur")
airplane5.PrintData()