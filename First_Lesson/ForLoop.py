friends = ["Jasmik", "Gerald", "Simona"]
for letter in "Python 2021":
    print(letter)

# --------------------

friends = ["Jasmik", "Gerald", "Simona"]
for friend in friends:
    print(friend)

# --------------------

for index in range(1, 5):
    print(index)

# -------------------

for index in range(len(friends)):
    print(friends[index])


# --------------------------------------

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result *= base_num

    return result


print(raise_to_power(3, 3))
