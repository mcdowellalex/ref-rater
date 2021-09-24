import requests

# used for asking for data
access_token=''

# used for asking for access token
accessTokenURL=''
authorization=''
content_type='application/x-www-form-urlencoded'
grant_type='client_credentials'

# asking for access token
response = requests.post(accessTokenURL, headers={'Authorization':authorization, 'Content-Type':content_type}, data={'grant_type':grant_type})
data = response.json()
access_token = data['access_token']
# print(access_token)


# get data
getRequestURL = 'https://football.elenasport.io/v2/countries'
getAuthorization = 'Bearer ' + access_token
response = requests.get(getRequestURL, headers={'Authorization':getAuthorization})

print(response.json())