import requests


response = requests.get("https://api.npoint.io/69c3d67fee24ce6ca0d5")
# response.raise_for_status()
data = response.json()

# print(int(data[0]['id']))

for post in data:
    if post['id'] == 1:
        print(post)
