'''
newfile = open('newfile.txt', "w+")

string = "This is a context thath will be written to the File"

newfile.write(string)
'''
import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size() != 0:
    old_file = open('./ages.json','r+')
    data = json.loads(old_file.read())
    print("Current Age is", data["age"])
else:
    old_file = open('./ages.json', "w+")
    data = {"name":"Aditya", "age":22}
    print("File not found")

old_file.seek(0)
old_file.write(json.dumps(data))