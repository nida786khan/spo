import requests
from bs4 import BeautifulSoup

username = input("Enter GitHub username: ")
url = f"https://github.com/{username}"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

image = soup.find("img", {"alt": "Avatar"})["src"]
print(f"Profile Image URL: {image}")
