# Imports
import random

# Names
class name:
    fName = []
    mName = {}
    lName = []

# Addresses
class street:
    streetName = []
    streetNum = random.randrange(100,9999)

# Locale
class locale:
    cityName = []
    cityZip = []
    state = []
    Contry = []

# Functions
def menu ():
    print("What data would you like to be generated?:")

print('-'*20 + " Data Generator "+ '-'*20)

menu()
while True:
    input()