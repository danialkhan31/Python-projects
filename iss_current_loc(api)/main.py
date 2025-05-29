import requests   #to get data from an api

#API For getting the current location of ISS
Key = "http://api.open-notify.org/iss-now.json"

response = requests.get(Key)
response.raise_for_status()   #raise an exception if HTTP request return an error status code
data = response.json()  #we will get the data as json (python dict)
loc = data['iss_position']

print(f"ISS Current location \nlongitude:{loc['longitude']} \nlatitude:{loc['latitude']}")