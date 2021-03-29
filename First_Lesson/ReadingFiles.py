


#---------writing  files in python

# w  overwriting all info
# a add line in to end
url = "C:\\Users\\hamlet.poghosyan\\Desktop\\Filerforpython1.txt"
json_first_file = open(url,"w")

json_first_file.writelines("\nSimona1 - English professor1")


json_first_file.close()

#---------reading files in python
# r for reading some info in file

url = "C:\\Users\\hamlet.poghosyan\\Desktop\\Filerforpython.txt"
json_first_file = open(url,"r")

print(json_first_file.read())

print("next")

for line1 in json_first_file.readlines():
    print(line1)

json_first_file.close()