import requests
import json

# ----------------- setup ------------------
# get auth data from auth file
with open('auth.json', 'r') as myfile:
    data=myfile.read()
    dataJSON = json.loads(data)
    authJSON = dataJSON['elenasport']

# used for asking for access token
accessTokenURL=authJSON['endpoint']
authorization=authJSON['authorization']
content_type=authJSON['content-type']
grant_type=authJSON['grant-type']

# ask for access token
response = requests.post(accessTokenURL, headers={'Authorization':authorization, 'Content-Type':content_type}, data={'grant_type':grant_type})
data = response.json()
access_token = data['access_token'] # used for API requests
# print(access_token)


# ----------------- HTTPS requests ------------------
getRequestURL = 'https://football.elenasport.io/v2/countries'
getAuthorization = 'Bearer ' + access_token
response = requests.get(getRequestURL, headers={'Authorization':getAuthorization})

print(response.json())


