from datetime import datetime

user_input = input("Enter your goal with a deadline separated by colon \n")
input_list = user_input.split(":")

goal = input_list[0]
dead_line= input_list[1]

dead_line_date = datetime.strptime(dead_line, "%d.%m.%Y")
today_date = datetime.today()

# calculation how many days from now till dateline
time_till = dead_line_date - today_date
hours_till = int(time_till.total_seconds() / 60 / 60)


print(f"Dear user! Time remaining for your goal : {goal} is {time_till.days} days , {hours_till} hours")

