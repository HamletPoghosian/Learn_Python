print("Work with lists")

friends = ["Jasmik", "Jack", "Bob"]

print(friends)

print(friends[0])

print(friends.index("Bob"))

print(friends[1:])  # get all start from 1 index

print(friends[1:3])  # get all start from 1 index end of 3

friends[0] = "Great Jasmik"

print(friends)

# list Function --------------------------

friends = ["Jasmik", "Jack", "Bob", "Walter", "Marry", "Vivien"]

lucky_numbers = [4, 8, 15, 16, 23, 42]

# extend add list to another list
friends.extend(lucky_numbers)

# append add only  | insert  add some index
friends.append("Simona")
friends.insert(5, "Gerald")

# remove()-  only one | clear()- all

friends.remove("Simona")
# friends.clear()
lucky_numbers.sort()
print(friends)

# -------------------Tuples------------

coordinates = (4, 5, 4)
print(coordinates)

coordinates_list = [(4, 5, 4), (10, 15, 32), (7, 8, 9)]
print(coordinates_list)


# -----------------Functions---------

def say_hi(name):
    print("Hello User " + name)


# name=input("input your name: ")
# say_hi(name)


def cube(num):
    return num * num * num


result = cube(4)
print(result)

# ----------if statments---

is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male")

elif is_male and not is_tall:
    print("You are a not male")

elif not is_male and not is_tall:
    print("You are a not male 1")

else:
    print("Yur are not a male  2")


#-----------2D list------

number_grid= [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)


