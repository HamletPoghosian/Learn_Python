from Chaf import Chaf
from ChinesChef import ChinesChef

myChef = Chaf()
myChef.make_chicken()
myChef.make_salad()

chines_Chef = ChinesChef()
chines_Chef.make_chicken()
chines_Chef.make_friend_rice()

user_input= input("enter numbers : ")

list_of_number=user_input.split(",")
print(list_of_number)
print(set(list_of_number))


print(type(list_of_number))
print(type(set(list_of_number)))


