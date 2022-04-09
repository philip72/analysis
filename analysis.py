import requests
from bs4 import BeautifulSoup

baseUrl = "https://www.jumia.co.ke"

headers = {
    'User': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 '
            'Safari/537.36 '
}
productlinks = []
productlinks.sort()
for x in range(1, 5):
    r = requests.get(f'https://www.jumia.co.ke/mlp-xiaomi-store/?page={x}#catalog-listing')
    soup = BeautifulSoup(r.content, 'lxml')
    productList = soup.find_all('article', class_='prd _fb col c-prd')  # collected items details
    for item in productList:
        for link in item.find_all('a', href=True):

            productlinks.append(baseUrl + link['href']) # this is to concatenate the stirngs that is the base url

# print(len(productlinks))  # prints out number of items in that page
# print(productlinks)
testLink= 'https://www.jumia.co.ke/xiaomi-redmi-9a-6.53-2gb32gb-13.0mp-5000mah-4g-lte-dual-sim-grey-30887170.html'
r=requests.get(testLink)
soup= BeautifulSoup(r.content,'lxml')
name =soup.find('h1', class_='-fs20 -pts -pbxs').text.strip()
rating = soup.find('div', class_='stars _s _al').text.strip()
review =soup.find('a', class_='-plxs _more',href="/catalog/productratingsreviews/sku/XI996MP049V77NAFAMZ/").text.strip()
price = soup.find('span', class_="-b -ltr -tal -fs24", dir='ltr').text.strip()
xiaomiProducts={
    'name': name,
    'rating':rating,
    'review':review,
    'price':price

}
print(xiaomiProducts)
