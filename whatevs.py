import json 
import requests 

# stalker 

r = requests.get('https://api.github.com/users/ArkAngeL43')

print(r)
print(r.content)
