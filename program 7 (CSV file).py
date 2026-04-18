#file handling with CSV file
#1.write to csv file

import csv
file=open("student.csv","w",newline='')
writer=csv.writer(file)
writer.writerow(["name","marks"])
writer.writerow(["Ali","98"])
file.close()


#2.read the csv file
file=open("student.csv","r")
reader=csv.reader(file)
for row in reader:
    print(row)
file.close()


#3.append the csv file
file=open("student.csv","a")
writer=csv.writer(file)
writer.writerow(["Ritesh","91"])
file.close()