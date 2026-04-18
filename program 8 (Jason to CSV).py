import json
import csv

json_file=open("a.json","r")
data=json.load(json_file)
json_file.close()

csv_file=open("b.csv","w",newline='')

header=data[0].keys()
writer=csv.Dictwriter(csv_file,fieldname=header)
writer.writeheader()
writer.writerows(data)

csv_file.close()