import requests
url=input("enter your url")
req=requests.get(url)
print(req.text)
