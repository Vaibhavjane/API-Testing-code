import requests
import json
import jsonpath
#API url
url="https://reqres.in/api/users/2"
#1) Read input json file
file=open("C:\\Users\\HP\\PycharmProjects\\pythonProject\\API Automation\\creatinguser.json",'r')
json_input= file.read()
#2) parse dat into json format
request_json=json.loads(json_input)
print(request_json)
#3) Make Post resquest with json input body
response=requests.put(url,request_json)
print(response.content)
#validating response code
assert response.status_code==200
print(response.headers.get('Content-Length'))
#parse respons to json format
response_json=json.loads(response.text)
#pick id from json path
id=jsonpath.jsonpath(response_json,'id')
print(id)
