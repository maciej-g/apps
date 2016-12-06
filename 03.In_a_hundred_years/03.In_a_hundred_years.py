# -*- coding: utf-8 -*-
from datetime import datetime
now = datetime.now()



name = str(input("What's your name?"))
try:
    age = int(input("How old are you?"))
    copy =int(input("How many copies of this message do you want?"))
    z = (now.year - age) +100
    for i in range(copy):
        print(name, ",when you'll have 100 years it will be year",z,)

except ValueError:
        print("Please enter an integer for an age!")