import requests
import json
import jsonpath
#API url
url="https://reqres.in/api/users?page=2"

#sendget request
requests.get(url)
response=requests.get(url)
#print(response)
#print(response.content)
#fetch response header
#print(response.headers.get('server'))
# fetch cookies
#print(response.cookies)
#fetch encoding
#print(response.encoding)
#print(response.elapsed)
# fetch response on jsonformat
json_response= json.loads(response.text)
#print(json_response)
# fetch values from json path
pages=jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])
assert pages[0]==2