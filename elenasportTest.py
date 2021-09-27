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
premLeagueID = 234   
PL_21_22_seasonID = 4210
 
getRequestURL = 'https://football.elenasport.io/v2/seasons/4210/fixtures?&from=2021-09-24&to=2021-09-25'
getAuthorization = 'Bearer ' + access_token
response = requests.get(getRequestURL, headers={'Authorization':getAuthorization})

print(response.json())


# gives fixtures for a season ID in a date range
# https://football.elenasport.io/v2/seasons/{seasonID}/fixtures?&from=YYYY-MM-DD&to=YYYY=MM-DD
# example: https://football.elenasport.io/v2/seasons/4210/fixtures?&from=2021-09-24&to=2021-09-25


# gives seasonID's for specified league ID
# https://football.elenasport.io/v2/leagues/{ID}/seasons
# example: https://football.elenasport.io/v2/leagues/234/seasons