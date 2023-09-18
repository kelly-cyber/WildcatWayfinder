import requests

# url = 'http://localhost:7071/api/CreateRecord'
url = 'https://functionappkelly.azurewebsites.net/api/createrecord'

title = {'title':'test'} # or whatever your data fields are
x = requests.post(url, json=title)
print ("response text:", x.text)
print ("response code:", x.status_code)


# url = 'http://localhost:7071/api/ReadRecords'
url = 'https://functionappkelly.azurewebsites.net/api/readrecords'
query = '{"title":"test"}'
response = requests.get(url, params={"query": query})
print ("response text:", response.text)
print ("response code:", response.status_code)

#test another string for title
# url = 'http://localhost:7071/api/CreateRecord'
url = 'https://functionappkelly.azurewebsites.net/api/createrecord'
title = {'title':'test2'} # or whatever your data fields are
x = requests.post (url, json=title)
print ("response text:", x. text)
print ("response code:", x.status_code)


# url = 'http://localhost:7071/api/ReadRecords'
url = 'https://functionappkelly.azurewebsites.net/api/readrecords'
query = '{"title":"test2"}'
response = requests.get(url, params={"query": query})
print ("response text:", response.text)
print ("response code:", response.status_code)
