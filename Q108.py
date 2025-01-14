import requests

response = requests.get("https://api.github.com")
if response.status_code == 200:
    print("GitHub API Data:")
    print(response.json())
else:
    print("Failed to fetch data.")
