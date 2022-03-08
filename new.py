import datetime
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"),end="")
print("000000")
import yaml

with open(r'C:\Users\ADMIN\Downloads\DataSet\Milestone1\Milestone1A.yaml') as file:
    documents = yaml.full_load(file)

    for item, doc in documents.items():
        print(item, ":", doc)