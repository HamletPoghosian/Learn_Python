#import Helper  -  same
#import Helper as H  -  same  every time H.Function()
#from Helper import *  - same  only think you dont need every time use Helper.

from Helper import validate_and_execute,user_inport_message # import only prefer function
import os
import logging as log

loger = log.getLogger("MAIN")
loger.error("ERROR")

print(os.name)

user_input = ""
while user_input!="exit":
    user_input=input(user_inport_message)
    days_and_unit= user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary={"days": days_and_unit[0],"unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute(days_and_unit_dictionary)




