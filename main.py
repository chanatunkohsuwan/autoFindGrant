import requests

url = "https://frc5190.com"

response = requests.get(url)

with open("output.out", "w+") as f:
    f.write(response.text)