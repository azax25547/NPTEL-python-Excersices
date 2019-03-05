import requests
import simplejson as json

'''
params = {"q": "pizza"}
r = requests.get('http://google.co.in/search', params=params)
print("Status", r.status_code)
# print(r.url)

f = open('page.html', 'w+')
f.write(r.text)

my_data = {"name":"aditya", "email":"mishra@gmail.com"}
r = requests.post('https://www.w3schools.com/php/welcome.php', data = my_data)

f = open('myfile.html', 'w+')
f.write(r.text)
'''
url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longUrl":"http://example.com"}
headers= {"Content-Type":"application/json"}
r = requests.post(url, json=payload, headers=headers)

print(r.headers)