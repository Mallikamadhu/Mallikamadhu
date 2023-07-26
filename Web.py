import requests
from bs4 import BeautifulSoup

# URL of the product page you want to scrape
url = "https://www.flipkart.com/milton-thermosteel-atlantis-400-water-bottle-ml/p/itmccd922ca771e2?pid=BOTF7JVWZ3H2DART&lid=LSTBOTF7JVWZ3H2DARTRTXKDU&marketplace=FLIPKART&cmpid=content_bottle_15083003945_u_8965229628_gmc_pla&tgi=sem,1,G,11214002,u,,,556262839325,,,,m,,mobile,,,,,&gclid=Cj0KCQjwjryjBhD0ARIsAMLvnF960TQPnbe1VPdSicbjFZ7p20-ZlQXM099w_coDy1TxBpYPGxufP1IaArwYEALw_wcB"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extracting the price
price = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
if price:
    price = price.text.strip()
else:
    price = "Price not available"

# Extracting the title
title = soup.find("span", {"class": "B_NuCI"})
if title:
    title = title.text.strip()
else:
    title = "Title not available"

# Extracting the reviews
reviews = soup.find("div", {"class": "_3LWZlK"})
if reviews:
    reviews = reviews.text.strip()
else:
    reviews = "No reviews available"

# Print the extracted information
print("Title:", title)
print("Price:", price)
print("Reviews:",reviews)