# Java Script Object Notation
import requests
import json


# URL = "https://swapi.dev/api/people/"
# response = requests.get(URL)

# if response.status_code == 200:
    # print(type(response.content))
    # print(type(response.text))
    
    # data = json.loads(response.text)
    # print(data)
    # print(type(data))    
    # json_string = json.dumps(data)
    # print(json_string)
    # print(type(json_string))
    
    
# peoples_data = dict()
    
# for endpoint in range(1, 12):
#     if endpoint == 17:
#         continue
    
#     print(f'Fetching info about people {endpoint}')
#     endpoint = str(endpoint)
#     response = requests.get(URL + endpoint + '/')
#     data = json.loads(response.text)
    
#     if data['eye_color']    == 'blue':
#         peoples_data[data['name']] = data['eye_color']         
        
# print(peoples_data)

# with open('data.json', 'w', encoding='utf-8') as json_file:
#     json.dump(peoples_data, json_file, indent=4)


# with open('data.json', 'r', encoding='utf-8') as json_file:
#     data = json.load(json_file)
    
# for key in data:
#     data[key] = 'black'
    
# with open('data.json', 'w', encoding='utf-8') as json_file:
#     json.dump(data, json_file, indent=4)



URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(URL).json()
print(response)