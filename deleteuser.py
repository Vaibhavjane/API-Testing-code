import requests

#API url
url="https://reqres.in/api/users/2"
response=requests.delete(url)
#Fetch Response code
print(response.status_code)
assert  response.status_code==204