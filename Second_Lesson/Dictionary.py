
def days_to_unites(number_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{number_of_days} day are {number_of_days * 24} hours "
    elif conversion_unit == "minutes":
        return f"{number_of_days} day are {number_of_days * 24 * 60} minutes "
    else:
        print("unsupported unit")


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_unites(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, please enter a valid positive number")
    except ValueError:
        print("please enter a valid positive number")

user_input = ""
while user_input!="exit":
    user_input=input("Hey user , enter number of days and conversion unit! \n")
    days_and_unit= user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary={"days":days_and_unit[0],"unit":days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()




