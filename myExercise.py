
import sys
file = open(sys.argv[1], "r", encoding = "utf-8")
names = []
uniandDepartment = []

for i in file:
    names.append(i.split(":")[0])
    uniandDepartment.append(i.split(":")[1])
file.close()

namesUniDict = dict(zip(names,uniandDepartment))

try:
    for i in sys.argv[2].split(","):
        university = namesUniDict[i]
        print("Name: " + str(i) +"\t" + "University: " + str(university))
except:

        print("No record of " + str(i) + " was found")





