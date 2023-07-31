from bs4 import BeautifulSoup
import json
import requests

STARTING_PAGE = 1
LAST_PAGE = -1
INCREMENT_COUNT = 1
FIRST_ELEMENT = 0
LAST_ELEMENT = -1

CATEGORIES = [
    "on-special", "dropped-locked", "back-to-school", 
    "meat-seafood", "fruit-vegetables", "bakery",
    "deli", "diary-eggs-fridge", "deli", "pantry",
    "drinks", "frozen", "household", "health-beauty",
    "baby", "pet", "liquor", "tobacco"
]

for category in range(STARTING_PAGE):
    url = f"https://www.coles.com.au/{CATEGORIES[category]}"

    # Signal get request to target url
    result = requests.get(url)

    # Parse the html
    doc = BeautifulSoup(result.text, "html.parser")

    num_of_pages = int(doc.find(role="status", class_="sr-only").text.split()[LAST_PAGE])

    items = []
    i = STARTING_PAGE
    while (i <= 1):
        url = f"https://www.coles.com.au/on-special?page={i}"
        result = requests.get(url)
        tags = doc.find_all(attrs={'data-testid': 'product-tile'}, class_="sc-6c766592-1 evKuUR coles-targeting-ProductTileProductTileWrapper")
        items.extend(tags)
        i += INCREMENT_COUNT
        
    json_arr = []
    for item in items:
        json_arr.append({
            "category": CATEGORIES[category],
            "href": item.find(class_="product__link")["href"],
            "imgName": item.find(class_="product__link")["href"].split("-")[LAST_ELEMENT],
            "imgSrc": item.find_all("img")[LAST_ELEMENT]["src"],
            "name": item.find("h2").text.split("|")[FIRST_ELEMENT].strip(),
            "price": float(item.find(class_="price__value").text.strip("$")),
            "unitPrice": item.find(class_="price__calculation_method").text
        })

    with open("coles.json", "w") as outfile:
        json.dump(json_arr, outfile)
        