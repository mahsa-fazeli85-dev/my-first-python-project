import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# عنوان صفحه
title = soup.title.get_text(strip=True)

print("عنوان صفحه:")
print(title)

# اطلاعات داخل یک کلاس خاص
print("\nعنوان بخش‌ها:")

sections = soup.select("div.mw-heading2 h2")

for section in sections:
    print(section.get_text(strip=True))

# لینک تصاویر
print("\nلینک تصاویر:")

images = soup.find_all("img")

for image in images[:10]:
    print(image.get("src"))