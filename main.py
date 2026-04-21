import requests

url = "https://frc5190.com"
print("responsinging")
response = requests.get(url)
# response.raise_for_status()
print("responsesd")

print(response)