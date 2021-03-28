mount_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Jul": "July",
    0:1,
}

print(mount_conversions["Jan"])

print(mount_conversions.get("Jan"))

print(mount_conversions.get("Jang", 'NewJang'))

print(mount_conversions[0])

