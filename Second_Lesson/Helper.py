def validate_and_execute(days_and_unit_dictionary):
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


def days_to_unites(number_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{number_of_days} day are {number_of_days * 24} hours "
    elif conversion_unit == "minutes":
        return f"{number_of_days} day are {number_of_days * 24 * 60} minutes "
    else:
        print("unsupported unit")


user_inport_message = "Hey user , enter number of days and conversion unit! \n"