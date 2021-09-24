import requests

url=''
authorization=''
content_type='application/x-www-form-urlencoded'
grant_type='client_credentials'

response = requests.post(url, headers={'Authorization':authorization, 'Content-Type':content_type}, data={'grant_type':grant_type})

print(response.json())